from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Build, RAM, CPU, Motherboard, Storage
from .serializers import BuildSerializer, MotherBoardSerializer, CPUSerializer, RAMSerializer, StorageSerializer
from .compatibility_service import CompatibilityService

@api_view(['POST'])
def create_build(request):
    """
    Create a new build with compatibility checks.
    """
    serializer = BuildSerializer(data=request.data)
    if serializer.is_valid():
        errors = check_compatibility(request.data)
        if errors:
            return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuildViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling build operations.
    """
    queryset = Build.objects.all()
    serializer_class = BuildSerializer

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
get_mobos = get_objects(Motherboard, MotherBoardSerializer)
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
