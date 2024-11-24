
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Build, Motherboard, CPU, RAM, Storage
from home.models import Storage, StorageType, Manufacturer, FormFactor, StorageCapacity
from .serializers import BuildSerializer, MotherboardSerializer, CPUSerializer, RAMSerializer, StorageSerializer
from .compatibility_service import CompatibilityService
from django.shortcuts import get_object_or_404 

# BuildViewSet: Manages CRUD operations for Builds.
class BuildViewSet(viewsets.ModelViewSet):
    queryset = Build.objects.all()  # QuerySet that returns all Build instances
    serializer_class = BuildSerializer  # Serializer to convert Build instances to JSON

    @action(detail=False, methods=['get'])
    def search(self, request):
        # Get search parameters from the request
        user_id = request.GET.get('user_id', None)
        user_username = request.GET.get('user_username', None)

        builds = Build.objects.all()  # Get all Build instances

        # Filter builds by user's ID if provided
        if user_id:
            builds = builds.filter(profile__user__id=user_id)
        # Filter builds by user's username if provided (case-insensitive)
        if user_username:
            builds = builds.filter(profile__user__username__iexact=user_username)

        serializer = BuildSerializer(builds, many=True)  # Serialize the filtered builds
        return Response(serializer.data)  # Return the serialized data as a response

# MotherboardViewSet: Manages CRUD operations for Motherboards.
class MotherboardViewSet(viewsets.ModelViewSet):
    queryset = Motherboard.objects.all()  # QuerySet that returns all Motherboard instances
    serializer_class = MotherboardSerializer  # Serializer to convert Motherboard instances to JSON

    @action(detail=False, methods=['get'])
    def search(self, request):
        # Get search parameters from the request
        manufacturer = request.GET.get('manufacturer', None)
        socket_type = request.GET.get('socket_type', None)

        motherboards = Motherboard.objects.all()  # Get all Motherboard instances

        # Filter motherboards by manufacturer if provided
        if manufacturer:
            motherboards = motherboards.filter(manufacturer__name__iexact=manufacturer)
        # Filter motherboards by socket type if provided
        if socket_type:
            motherboards = motherboards.filter(cpu_socket_type__name__iexact=socket_type)

        serializer = MotherboardSerializer(motherboards, many=True)  # Serialize the filtered motherboards
        return Response(serializer.data)  # Return the serialized data as a response

# CPUViewSet: Manages CRUD operations for CPUs.
class CPUViewSet(viewsets.ModelViewSet):
    queryset = CPU.objects.all()  # QuerySet that returns all CPU instances
    serializer_class = CPUSerializer  # Serializer to convert CPU instances to JSON

    @action(detail=False, methods=['get'])
    def search(self, request):
        # Get search parameters from the request
        socket_type = request.GET.get('socket_type', None)
        manufacturer = request.GET.get('manufacturer', None)
        microarchitecture = request.GET.get('microarchitecture', None)

        cpus = CPU.objects.all()  # Get all CPU instances

        # Filter CPUs by socket type if provided (case-insensitive)
        if socket_type:
            cpus = cpus.filter(socket_type__name__iexact=socket_type)
        # Filter CPUs by manufacturer if provided (case-insensitive)
        if manufacturer:
            cpus = cpus.filter(manufacturer__name__iexact=manufacturer)
        # Filter CPUs by microarchitecture if provided (case-insensitive)
        if microarchitecture:
            cpus = cpus.filter(microarchitecture__iexact=microarchitecture)

        serializer = CPUSerializer(cpus, many=True)  # Serialize the filtered CPUs
        return Response(serializer.data)  # Return the serialized data as a response

# RAMViewSet: Manages CRUD operations for RAM.
class RAMViewSet(viewsets.ModelViewSet):
    queryset = RAM.objects.all()  # QuerySet that returns all RAM instances
    serializer_class = RAMSerializer  # Serializer to convert RAM instances to JSON

    @action(detail=False, methods=['get'])
    def search(self, request):
        # Get search parameters from the request
        memory_type = request.GET.get('memory_type', None)
        speed = request.GET.get('speed', None)
        capacity = request.GET.get('capacity', None)
        number_of_modules = request.GET.get('number_of_modules', None)
        manufacturer = request.GET.get('manufacturer', None)

        rams = RAM.objects.all()  # Get all RAM instances

        # Filter RAMs by memory type if provided (case-insensitive)
        if memory_type:
            rams = rams.filter(type__iexact=memory_type)
        # Filter RAMs by speed if provided (case-insensitive)
        if speed:
            rams = rams.filter(speed__iexact=speed)
        # Filter RAMs by capacity if provided (exact match)
        if capacity:
            rams = rams.filter(capacity=capacity)
        # Filter RAMs by number of modules if provided (exact match)
        if number_of_modules:
            rams = rams.filter(number_of_modules=number_of_modules)
        # Filter RAMs by manufacturer if provided (case-insensitive)
        if manufacturer:
            rams = rams.filter(manufacturer__name__iexact=manufacturer)

        serializer = RAMSerializer(rams, many=True)  # Serialize the filtered RAMs
        return Response(serializer.data)  # Return the serialized data as a response

# StorageViewSet: Manages CRUD operations for Storage.
class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()  # QuerySet that returns all Storage instances
    serializer_class = StorageSerializer  # Serializer to convert Storage instances to JSON

    @action(detail=False, methods=['get'])
    def search(self, request):
        # Get search parameters from the request
        manufacturer = request.GET.get('manufacturer', None)
        form_factor = request.GET.get('form_factor', None)
        capacity = request.GET.get('capacity', None)
        storage_type = request.GET.get('type', None)  # Renamed variable to avoid shadowing built-in type

        storages = Storage.objects.all()  # Get all Storage instances

        # Filter storage by manufacturer if provided
        if manufacturer:
            storages = storages.filter(manufacturer__name__exact=manufacturer)
        # Filter storage by form factor if provided
        if form_factor:
            storages = storages.filter(form_factor__name__exact=form_factor)
        # Filter storage by capacity if provided
        if capacity:
            storage_capacity = get_object_or_404(StorageCapacity, capacity=capacity)  # Ensure capacity exists
            storages = storages.filter(capacity=storage_capacity)
        # Filter storage by type if provided
        if storage_type:
            storage_type_obj = get_object_or_404(StorageType, type__exact=storage_type)  # Ensure type exists
            storages = storages.filter(type=storage_type_obj)

        serializer = StorageSerializer(storages, many=True)  # Serialize the filtered storages
        return Response(serializer.data)  # Return the serialized data as a response

# UserBuildViewSet: Manages listing builds for a specific user.
class UserBuildViewSet(viewsets.ViewSet):
    def xǁUserBuildViewSetǁlist__mutmut_orig(self, request, user_id=None):
        try:
            queryset = Build.objects.filter(profile__user__id=user_id)  # Filter builds by user's ID through profile
            serializer = BuildSerializer(queryset, many=True)  # Serialize the filtered builds
            return Response(serializer.data)  # Return the serialized data as a response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return error response if exception occurs
    def xǁUserBuildViewSetǁlist__mutmut_1(self, request, user_id=None):
        try:
            queryset = Build.objects.filter(profile__user__id=None)  # Filter builds by user's ID through profile
            serializer = BuildSerializer(queryset, many=True)  # Serialize the filtered builds
            return Response(serializer.data)  # Return the serialized data as a response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return error response if exception occurs
    def xǁUserBuildViewSetǁlist__mutmut_2(self, request, user_id=None):
        try:
            queryset = None  # Filter builds by user's ID through profile
            serializer = BuildSerializer(queryset, many=True)  # Serialize the filtered builds
            return Response(serializer.data)  # Return the serialized data as a response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return error response if exception occurs
    def xǁUserBuildViewSetǁlist__mutmut_3(self, request, user_id=None):
        try:
            queryset = Build.objects.filter(profile__user__id=user_id)  # Filter builds by user's ID through profile
            serializer = BuildSerializer(None, many=True)  # Serialize the filtered builds
            return Response(serializer.data)  # Return the serialized data as a response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return error response if exception occurs
    def xǁUserBuildViewSetǁlist__mutmut_4(self, request, user_id=None):
        try:
            queryset = Build.objects.filter(profile__user__id=user_id)  # Filter builds by user's ID through profile
            serializer = BuildSerializer(queryset, many=False)  # Serialize the filtered builds
            return Response(serializer.data)  # Return the serialized data as a response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return error response if exception occurs
    def xǁUserBuildViewSetǁlist__mutmut_5(self, request, user_id=None):
        try:
            queryset = Build.objects.filter(profile__user__id=user_id)  # Filter builds by user's ID through profile
            serializer = BuildSerializer( many=True)  # Serialize the filtered builds
            return Response(serializer.data)  # Return the serialized data as a response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return error response if exception occurs
    def xǁUserBuildViewSetǁlist__mutmut_6(self, request, user_id=None):
        try:
            queryset = Build.objects.filter(profile__user__id=user_id)  # Filter builds by user's ID through profile
            serializer = BuildSerializer(queryset,)  # Serialize the filtered builds
            return Response(serializer.data)  # Return the serialized data as a response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return error response if exception occurs
    def xǁUserBuildViewSetǁlist__mutmut_7(self, request, user_id=None):
        try:
            queryset = Build.objects.filter(profile__user__id=user_id)  # Filter builds by user's ID through profile
            serializer = None  # Serialize the filtered builds
            return Response(serializer.data)  # Return the serialized data as a response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return error response if exception occurs
    def xǁUserBuildViewSetǁlist__mutmut_8(self, request, user_id=None):
        try:
            queryset = Build.objects.filter(profile__user__id=user_id)  # Filter builds by user's ID through profile
            serializer = BuildSerializer(queryset, many=True)  # Serialize the filtered builds
            return Response(serializer.data)  # Return the serialized data as a response
        except Exception as e:
            return Response({'XXerrorXX': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return error response if exception occurs
    def xǁUserBuildViewSetǁlist__mutmut_9(self, request, user_id=None):
        try:
            queryset = Build.objects.filter(profile__user__id=user_id)  # Filter builds by user's ID through profile
            serializer = BuildSerializer(queryset, many=True)  # Serialize the filtered builds
            return Response(serializer.data)  # Return the serialized data as a response
        except Exception as e:
            return Response({'error': str(None)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return error response if exception occurs
    def xǁUserBuildViewSetǁlist__mutmut_10(self, request, user_id=None):
        try:
            queryset = Build.objects.filter(profile__user__id=user_id)  # Filter builds by user's ID through profile
            serializer = BuildSerializer(queryset, many=True)  # Serialize the filtered builds
            return Response(serializer.data)  # Return the serialized data as a response
        except Exception as e:
            return Response({'error': str(e)},)  # Return error response if exception occurs

    xǁUserBuildViewSetǁlist__mutmut_mutants = {
    'xǁUserBuildViewSetǁlist__mutmut_1': xǁUserBuildViewSetǁlist__mutmut_1, 
        'xǁUserBuildViewSetǁlist__mutmut_2': xǁUserBuildViewSetǁlist__mutmut_2, 
        'xǁUserBuildViewSetǁlist__mutmut_3': xǁUserBuildViewSetǁlist__mutmut_3, 
        'xǁUserBuildViewSetǁlist__mutmut_4': xǁUserBuildViewSetǁlist__mutmut_4, 
        'xǁUserBuildViewSetǁlist__mutmut_5': xǁUserBuildViewSetǁlist__mutmut_5, 
        'xǁUserBuildViewSetǁlist__mutmut_6': xǁUserBuildViewSetǁlist__mutmut_6, 
        'xǁUserBuildViewSetǁlist__mutmut_7': xǁUserBuildViewSetǁlist__mutmut_7, 
        'xǁUserBuildViewSetǁlist__mutmut_8': xǁUserBuildViewSetǁlist__mutmut_8, 
        'xǁUserBuildViewSetǁlist__mutmut_9': xǁUserBuildViewSetǁlist__mutmut_9, 
        'xǁUserBuildViewSetǁlist__mutmut_10': xǁUserBuildViewSetǁlist__mutmut_10
    }

    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserBuildViewSetǁlist__mutmut_orig"), object.__getattribute__(self, "xǁUserBuildViewSetǁlist__mutmut_mutants"), *args, **kwargs)
        return result 

    list.__signature__ = _mutmut_signature(xǁUserBuildViewSetǁlist__mutmut_orig)
    xǁUserBuildViewSetǁlist__mutmut_orig.__name__ = 'xǁUserBuildViewSetǁlist'


