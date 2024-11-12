from django.core.exceptions import ValidationError
from home.models import CPUMotherboardCompatibility, SupportedRAMConfiguration, SupportedStorageConfiguration  # Import necessary models

class CompatibilityService:
    """
    CompatibilityService is a utility class that provides static methods
    to check compatibility between different components of a build.
    """

    @staticmethod
    def check_build_compatibility(build):
        """
        Check the overall compatibility of the build by delegating to individual
        component compatibility checks.

        Args:
            build (Build): The build object containing the components to be checked.

        Returns:
            (bool, list): A tuple containing a boolean indicating overall compatibility
                          and a list of issues found.
        """
        # Check CPU compatibility
        cpu_compatible, cpu_issues = CompatibilityService.check_cpu_compatibility(build)
        # Check RAM compatibility
        ram_compatible, ram_issues = CompatibilityService.check_ram_compatibility(build)
        # Check storage compatibility
        storage_compatible, storage_issues = CompatibilityService.check_storage_compatibility(build)
        
        # Determine overall compatibility
        compatible = cpu_compatible and ram_compatible and storage_compatible
        # Collect all issues
        issues = cpu_issues + ram_issues + storage_issues
        
        return compatible, issues

    @staticmethod
    def check_cpu_compatibility(build):
        """
        Check the compatibility between the CPU and the motherboard.

        Args:
            build (Build): The build object containing the components to be checked.

        Returns:
            (bool, list): A tuple containing a boolean indicating CPU compatibility
                          and a list of issues found.
        """
        # Get the motherboard and CPU from the build
        motherboard = build.motherboard
        cpu = build.cpu
        issues = []

        # Check if both motherboard and CPU are present
        if motherboard and cpu:
            # Check if the CPU is compatible with the motherboard
            if not CPUMotherboardCompatibility.objects.filter(cpu=cpu, motherboard=motherboard).exists():
                issues.append("The selected CPU is not compatible with the motherboard.")
        
        return not issues, issues

    @staticmethod
    def check_ram_compatibility(build):
        """
        Check the compatibility between RAM modules and the motherboard.

        Args:
            build (Build): The build object containing the components to be checked.

        Returns:
            (bool, list): A tuple containing a boolean indicating RAM compatibility
                          and a list of issues found.
        """
        # Get the motherboard and RAM modules from the build
        motherboard = build.motherboard
        ram_modules = build.ram.all()
        issues = []

        def parse_capacity(ram_capacity):
            """
            Helper function to parse RAM capacity from string to integer.

            Args:
                ram_capacity (str): The RAM capacity string (e.g., '16GB').

            Returns:
                int: The RAM capacity in GB.
            """
            return int(ram_capacity.rstrip('GB'))

        # Calculate the total RAM capacity and number of modules
        total_ram_capacity = sum(parse_capacity(ram_module.ram_capacity.capacity) for ram_module in ram_modules)
        total_ram_modules = sum(int(ram_module.ram_number_of_modules.number_of_modules) for ram_module in ram_modules)

        # Check if both motherboard and RAM modules are present
        if motherboard and ram_modules.exists():
            # Check if each RAM module is supported by the motherboard
            for ram_module in ram_modules:
                if not SupportedRAMConfiguration.objects.filter(motherboard=motherboard, ram=ram_module).exists():
                    issues.append(f"RAM module {ram_module} is not supported by the motherboard {motherboard.name}.")
            # Check if total RAM capacity exceeds the motherboard's maximum capacity
            if total_ram_capacity > int(motherboard.max_memory_capacity):
                issues.append(f"The total RAM capacity ({total_ram_capacity} GB) exceeds the maximum capacity of the motherboard ({motherboard.max_memory_capacity} GB).")
            # Check if total number of RAM modules exceeds the number of slots on the motherboard
            if total_ram_modules > int(motherboard.memory_slots):
                issues.append(f"The total number of RAM modules ({total_ram_modules}) exceeds the number of slots on the motherboard ({motherboard.memory_slots}).")

        return not issues, issues

    @staticmethod
    def check_storage_compatibility(build):
        """
        Check the compatibility between storage devices and the motherboard.

        Args:
            build (Build): The build object containing the components to be checked.

        Returns:
            (bool, list): A tuple containing a boolean indicating storage compatibility
                          and a list of issues found.
        """
        # Get the motherboard and storage devices from the build
        motherboard = build.motherboard
        storages = build.storages.all()
        issues = []

        # Check if both motherboard and storage devices are present
        if motherboard and storages.exists():
            # Check if each storage device is supported by the motherboard
            for storage_device in storages:
                supported_storage_config = SupportedStorageConfiguration.objects.filter(motherboard=motherboard, storage_type=storage_device.type).first()
                if not supported_storage_config:
                    issues.append(f"Storage type {storage_device.type} is not supported by the motherboard.")
                # Check if the storage device's form factor is supported by the motherboard
                elif storage_device.form_factor not in supported_storage_config.supported_form_factors:
                    issues.append(f"Storage form factor {storage_device.form_factor} is not supported by the motherboard.")
        
        return not issues, issues
