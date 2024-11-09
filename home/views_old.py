from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Build, RAM, CPU, Motherboard, Storage
from .serializers import BuildSerializer, MotherBoardSerializer, CPUSerializer, RAMSerializer, StorageSerializer

# API endpoint views
class BuildViewSet(viewsets.ModelViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer

@api_view(['GET'])
def get_mobos(request):
    try:
        queryset = Motherboard.objects.all()
        serializer = MotherBoardSerializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_cpus(request):
    try:
        queryset = CPU.objects.all()
        serializer = CPUSerializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_builds(request):
    try:
        queryset = Build.objects.all()
        serializer = BuildSerializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_builds_user(request, user_id):
    try:
        queryset = Build.objects.filter(profile__user__id=user_id)
        serializer = BuildSerializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_rams(request):
    try:
        queryset = RAM.objects.all()
        serializer = RAMSerializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_storages(request):
    try:
        queryset = Storage.objects.all()
        serializer = StorageSerializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
