# compatibility_service.py

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
        cpu_compatible, cpu_issues = CompatibilityService.check_cpu_compatibility(build)
        ram_compatible, ram_issues = CompatibilityService.check_ram_compatibility(build)
        storage_compatible, storage_issues = CompatibilityService.check_storage_compatibility(build)
        
        compatible = cpu_compatible and ram_compatible and storage_compatible
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
        motherboard = build.motherboard
        cpu = build.cpu
        issues = []

        if motherboard and cpu:
            if motherboard.cpu_socket_type != cpu.socket_type:
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

        total_ram_capacity = sum(parse_capacity(ram_module.ram_capacity.capacity) for ram_module in ram_modules)
        total_ram_modules = sum(int(ram_module.ram_number_of_modules.number_of_modules) for ram_module in ram_modules)

        if motherboard and ram_modules.exists():
            for ram_module in ram_modules:
                if ram_module.ram_type not in motherboard.supported_ram_types.all():
                    issues.append(f"RAM type {ram_module.ram_type} is not supported by the motherboard {motherboard.name}.")
                if ram_module.ram_speed not in motherboard.supported_ram_speeds.all():
                    issues.append(f"RAM speed {ram_module.ram_speed} is not supported by the motherboard {motherboard.name}.")
            if total_ram_capacity > int(motherboard.max_memory_capacity):
                issues.append(f"The total RAM capacity ({total_ram_capacity} GB) exceeds the maximum capacity of the motherboard ({motherboard.max_memory_capacity} GB).")
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
        motherboard = build.motherboard
        storage = build.storage.all()
        issues = []

        if motherboard and storage.exists():
            for storage_device in storage:
                if storage_device.type not in motherboard.supported_storage_types.all():
                    issues.append(f"Storage type {storage_device.type} is not supported by the motherboard.")
                if storage_device.form_factor not in motherboard.storage_form_factor.all():
                    issues.append(f"Storage form factor {storage_device.form_factor} is not supported by the motherboard.")
        
        return not issues, issues
