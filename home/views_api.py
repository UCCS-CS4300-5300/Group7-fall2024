from django.core.cache import cache
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from home.models import Build, Motherboard, CPU, RAM, Storage, StorageType, Manufacturer, FormFactor, StorageCapacity
from .serializers import BuildSerializer, MotherboardSerializer, CPUSerializer, RAMSerializer, StorageSerializer
from .compatibility_service import CompatibilityService
from django.shortcuts import get_object_or_404
import logging


# Set up logging configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # You can adjust the level based on your needs

# Create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to console handler
ch.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(ch)


def filter_by_field(queryset, field_name, value, lookup='iexact'):
    """
    Helper function to filter a queryset by a specific field.

    Args:
        queryset: The queryset to filter.
        field_name: The name of the field to filter by.
        value: The value to filter the field by.
        lookup: The lookup type (default: 'iexact').

    Returns:
        The filtered queryset.
    """
    if value:
        filter_kwargs = {f"{field_name}__{lookup}": value}
        return queryset.filter(**filter_kwargs)
    return queryset


# Define a custom pagination class
class CustomPagination(PageNumberPagination):
    """
    CustomPagination: Defines the default page size and query parameters for pagination.
    """
    page_size = 10  # Default page size
    page_size_query_param = 'page_size'
    max_page_size = 100


# ViewSet for managing Builds
class BuildViewSet(viewsets.ModelViewSet):
    """
    BuildViewSet: Manages CRUD operations for Builds.
    """
    queryset = Build.objects.all()
    serializer_class = BuildSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Search for builds by user ID or username.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the filtered builds.
        """
        user_id = request.GET.get('user_id', None)
        user_username = request.GET.get('user_username', None)

        # Validate user_id
        if user_id is not None and not user_id.isdigit():
            raise ValidationError({"user_id": "user_id must be a valid integer."})

        # Validate user_username
        if user_username is not None and not isinstance(user_username, str):
            raise ValidationError({"user_username": "user_username must be a valid string."})

        cache_key = f"builds_search_{user_id}_{user_username}"
        cached_results = cache.get(cache_key)

        if cached_results:
            logger.info(f"Cache hit for key: {cache_key}")
            return Response(cached_results)

        builds = Build.objects.all()

        try:
            builds = filter_by_field(builds, 'profile__user__id', user_id, lookup='exact')
            builds = filter_by_field(builds, 'profile__user__username', user_username, lookup='iexact')
        except Exception as e:
            logger.error(f"Error during search: {e}")
            return Response({'error': 'An error occurred during the search.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        paginator = CustomPagination()
        paginated_results = paginator.paginate_queryset(builds, request)
        serializer = BuildSerializer(paginated_results, many=True)
        cache.set(cache_key, serializer.data, timeout=300)  # Cache for 5 minutes
        logger.info(f"Search results returned for user_id: {user_id}, user_username: {user_username}")
        return paginator.get_paginated_response(serializer.data)


# ViewSet for managing Motherboards
class MotherboardViewSet(viewsets.ModelViewSet):
    """
    MotherboardViewSet: Manages CRUD operations for Motherboards.
    """
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Search for motherboards by manufacturer or socket type.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the filtered motherboards.
        """
        manufacturer = request.GET.get('manufacturer', None)
        socket_type = request.GET.get('socket_type', None)

        # Validate manufacturer
        if manufacturer is not None and not isinstance(manufacturer, str):
            raise ValidationError({"manufacturer": "manufacturer must be a valid string."})

        # Validate socket_type
        if socket_type is not None and not isinstance(socket_type, str):
            raise ValidationError({"socket_type": "socket_type must be a valid string."})

        cache_key = f"motherboards_search_{manufacturer}_{socket_type}"
        cached_results = cache.get(cache_key)

        if cached_results:
            logger.info(f"Cache hit for key: {cache_key}")
            return Response(cached_results)

        motherboards = Motherboard.objects.all()

        try:
            motherboards = filter_by_field(motherboards, 'manufacturer__name', manufacturer, lookup='iexact')
            motherboards = filter_by_field(motherboards, 'cpu_socket_type__name', socket_type, lookup='iexact')
        except Exception as e:
            logger.error(f"Error during search: {e}")
            return Response({'error': 'An error occurred during the search.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        paginator = CustomPagination()
        paginated_results = paginator.paginate_queryset(motherboards, request)
        serializer = MotherboardSerializer(paginated_results, many=True)
        cache.set(cache_key, serializer.data, timeout=300)  # Cache for 5 minutes
        logger.info(f"Search results returned for manufacturer: {manufacturer}, socket_type: {socket_type}")
        return paginator.get_paginated_response(serializer.data)


# ViewSet for managing CPUs
class CPUViewSet(viewsets.ModelViewSet):
    """
    CPUViewSet: Manages CRUD operations for CPUs.
    """
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Search for CPUs by socket type, manufacturer, or microarchitecture.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the filtered CPUs.
        """
        socket_type = request.GET.get('socket_type', None)
        manufacturer = request.GET.get('manufacturer', None)
        microarchitecture = request.GET.get('microarchitecture', None)

        # Validate socket_type
        if socket_type is not None and not isinstance(socket_type, str):
            raise ValidationError({"socket_type": "socket_type must be a valid string."})

        # Validate manufacturer
        if manufacturer is not None and not isinstance(manufacturer, str):
            raise ValidationError({"manufacturer": "manufacturer must be a valid string."})

        # Validate microarchitecture
        if microarchitecture is not None and not isinstance(microarchitecture, str):
            raise ValidationError({"microarchitecture": "microarchitecture must be a valid string."})

        cache_key = f"cpus_search_{socket_type}_{manufacturer}_{microarchitecture}"
        cached_results = cache.get(cache_key)

        if cached_results:
            logger.info(f"Cache hit for key: {cache_key}")
            return Response(cached_results)

        cpus = CPU.objects.all()

        try:
            cpus = filter_by_field(cpus, 'socket_type__name', socket_type, lookup='iexact')
            cpus = filter_by_field(cpus, 'manufacturer__name', manufacturer, lookup='iexact')
            cpus = filter_by_field(cpus, 'microarchitecture', microarchitecture, lookup='iexact')
        except Exception as e:
            logger.error(f"Error during search: {e}")
            return Response({'error': 'An error occurred during the search.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        paginator = CustomPagination()
        paginated_results = paginator.paginate_queryset(cpus, request)
        serializer = CPUSerializer(paginated_results, many=True)
        cache.set(cache_key, serializer.data, timeout=300)  # Cache for 5 minutes
        logger.info(f"Search results returned for socket_type: {socket_type}, manufacturer: {manufacturer}, microarchitecture: {microarchitecture}")
        return paginator.get_paginated_response(serializer.data)


class RAMViewSet(viewsets.ModelViewSet):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        ram_type = request.GET.get('type', None)
        capacity = request.GET.get('capacity', None)
        speed = request.GET.get('speed', None)
        number_of_modules = request.GET.get('number_of_modules', None)
        manufacturer = request.GET.get('manufacturer', None)

        cache_key = f"rams_search_{ram_type}_{capacity}_{speed}_{number_of_modules}_{manufacturer}".replace(' ', '_')
        cached_results = cache.get(cache_key)

        if cached_results:
            return Response(cached_results)

        rams = RAM.objects.all()

        if ram_type:
            rams = rams.filter(ram_type__type=ram_type)
        if capacity:
            rams = rams.filter(ram_capacity__capacity=capacity)
        if speed:
            rams = rams.filter(ram_speed__speed=speed)
        if number_of_modules:
            rams = rams.filter(ram_number_of_modules__number_of_modules=number_of_modules)
        if manufacturer:
            rams = rams.filter(manufacturer__name=manufacturer)

        paginator = PageNumberPagination()
        paginated_results = paginator.paginate_queryset(rams, request, view=self)
        if paginated_results is not None:
            serializer = RAMSerializer(paginated_results, many=True)
            cache.set(cache_key, serializer.data, timeout=300)
            return paginator.get_paginated_response(serializer.data)

        serializer = RAMSerializer(rams, many=True)
        return Response(serializer.data)


class StorageViewSet(viewsets.ModelViewSet):
    """
    StorageViewSet: Manages CRUD operations for Storage.
    """
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Search for storage by manufacturer, form factor, capacity, or storage type.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the filtered storage.
        """
        manufacturer = request.GET.get('manufacturer', None)
        form_factor = request.GET.get('form_factor', None)
        capacity = request.GET.get('capacity', None)
        storage_type = request.GET.get('type', None)  # Renamed variable to avoid shadowing built-in type

        # Validate manufacturer
        if manufacturer is not None and not isinstance(manufacturer, str):
            raise ValidationError({"manufacturer": "manufacturer must be a valid string."})

        # Validate form_factor
        if form_factor is not None and not isinstance(form_factor, str):
            raise ValidationError({"form_factor": "form_factor must be a valid string."})

        # Validate capacity
        if capacity is not None and not capacity.isdigit():
            raise ValidationError({"capacity": "capacity must be a valid integer."})

        # Validate storage_type
        if storage_type is not None and not isinstance(storage_type, str):
            raise ValidationError({"storage_type": "storage_type must be a valid string."})

        cache_key = f"storages_search_{manufacturer}_{form_factor}_{capacity}_{storage_type}".replace(' ', '_')
        cached_results = cache.get(cache_key)

        if cached_results:
            logger.info(f"Cache hit for key: {cache_key}")
            return Response(cached_results)

        storages = Storage.objects.all().order_by('storage_id')  # Ensure ordered query set

        try:
            storages = filter_by_field(storages, 'manufacturer__name', manufacturer, lookup='exact')
            storages = filter_by_field(storages, 'form_factor__name', form_factor, lookup='exact')
            if capacity:
                storage_capacity = get_object_or_404(StorageCapacity, capacity=capacity)  # Ensure capacity exists
                storages = storages.filter(capacity=storage_capacity)
            storages = filter_by_field(storages, 'type__type', storage_type, lookup='exact')
        except Exception as e:
            logger.error(f"Error during search: {e}")
            return Response({'error': 'An error occurred during the search.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        paginator = CustomPagination()
        paginated_results = paginator.paginate_queryset(storages, request)
        serializer = StorageSerializer(paginated_results, many=True)
        cache.set(cache_key, serializer.data, timeout=300)  # Cache for 5 minutes
        logger.info(f"Search results returned for manufacturer: {manufacturer}, form_factor: {form_factor}, capacity: {capacity}, storage_type: {storage_type}")
        return paginator.get_paginated_response(serializer.data)


# ViewSet for managing a user's Builds
class UserBuildViewSet(viewsets.ViewSet):
    """
    UserBuildViewSet: Manages listing builds for a specific user.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        List builds for the authenticated user.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response containing the user's builds or an error message.
        """
        user_id = kwargs.get('user_id')
        cache_key = f"user_builds_{user_id}"
        cached_results = cache.get(cache_key)

        if cached_results:
            logger.info(f"Cache hit for key: {cache_key}")
            return Response(cached_results)

        try:
            queryset = Build.objects.filter(profile__user__id=user_id)  # Filter builds by user's ID through profile

            paginator = CustomPagination()
            paginated_results = paginator.paginate_queryset(queryset, request)

            serializer = BuildSerializer(paginated_results, many=True)  # Serialize the filtered builds
            cache.set(cache_key, serializer.data, timeout=300)  # Cache for 5 minutes
            logger.info(f"Listing builds for user_id: {user_id}")
            return paginator.get_paginated_response(serializer.data)  # Return the paginated response
        except Exception as e:
            logger.error(f"Error listing builds for user_id {user_id}: {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return error response if exception occurs
