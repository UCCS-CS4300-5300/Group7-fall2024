from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Build, RAM, CPU, Motherboard, Storage
from .serializers import BuildSerializer, MotherboardSerializer, CPUSerializer, RAMSerializer, StorageSerializer
from .compatibility_service import CompatibilityService

@api_view(['POST'])
def create_build(request):
    """
    Create a new build with compatibility checks.
    """
    serializer = BuildSerializer(data=request.data)
    if serializer.is_valid():
        # Ensure compatibility
        build = Build(
            cpu=CPU.objects.get(id=request.data['cpu']),
            motherboard=Motherboard.objects.get(id=request.data['motherboard']),
        )
        build.ram.set(RAM.objects.filter(id__in=request.data['ram']))
        build.storage.set(Storage.objects.filter(id__in=request.data['storage']))

        compatible, issues = CompatibilityService.check_build_compatibility(build)
        if not compatible:
            return Response({'errors': issues}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuildViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling build operations.
    """
    queryset = Build.objects.all()
    serializer_class = BuildSerializer

class MotherboardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling motherboard operations.
    """
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer

class CPUViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CPU operations.
    """
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer

class RAMViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling RAM operations.
    """
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer

class StorageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling storage operations.
    """
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

def get_objects(model, serializer_class):
    """
    Generic function to get all objects of a model.
    """
    @api_view(['GET'])
    def view_function(request):
        try:
            queryset = model.objects.all()
            serializer = serializer_class(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return view_function

# API endpoint views using the generic function
get_mobos = get_objects(Motherboard, MotherboardSerializer)
get_cpus = get_objects(CPU, CPUSerializer)
get_builds = get_objects(Build, BuildSerializer)
get_rams = get_objects(RAM, RAMSerializer)
get_storages = get_objects(Storage, StorageSerializer)

@api_view(['GET'])
def get_builds_user(request, user_id):
    """
    Get builds for a specific user.
    """
    try:
        queryset = Build.objects.filter(profile__user__id=user_id)
        serializer = BuildSerializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Search views
@api_view(['GET'])
def search_motherboards(request):
    """
    Search for motherboards based on query parameters.
    """
    ram_type = request.query_params.get('ram_type', None)
    if ram_type:
        motherboards = Motherboard.objects.filter(supported_ram_types__type__iexact=ram_type)
    else:
        motherboards = Motherboard.objects.all()
    
    serializer = MotherboardSerializer(motherboards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_cpus(request):
    """
    Search for CPUs based on query parameters.
    """
    socket_type = request.query_params.get('socket_type', None)
    if socket_type:
        cpus = CPU.objects.filter(socket_type__name__iexact=socket_type)
    else:
        cpus = CPU.objects.all()
    
    serializer = CPUSerializer(cpus, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_rams(request):
    """
    Search for RAMs based on query parameters.
    """
    memory_type = request.query_params.get('memory_type', None)
    if memory_type:
        rams = RAM.objects.filter(ram_type__type__iexact=memory_type)
    else:
        rams = RAM.objects.all()
    
    serializer = RAMSerializer(rams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_storages(request):
    """
    Search for storages based on query parameters.
    """
    storage_type = request.query_params.get('storage_type', None)
    if storage_type:
        storages = Storage.objects.filter(storage_type__type__iexact=storage_type)
    else:
        storages = Storage.objects.all()
    
    serializer = StorageSerializer(storages, many=True)
    return Response(serializer.data)
