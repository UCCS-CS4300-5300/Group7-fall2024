class CompatibilityService:
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
        isValid = True
        issues = []

        if motherboard and cpu:
            if not motherboard.cpu_socket_type == cpu.socket_type:
                issues.append(f"The selected CPU is not compatible with the motherboard\nCPU has socket type: {cpu.socket_type}\nMotherboard has socket type: {motherboard.cpu_socket_type}")
                isValid = False

        return isValid, issues


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
        motherboard_supported_rams = motherboard.supportedramconfiguration_set.all()
        ram_modules = build.ram.all()
        isValid = True
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
        total_ram_modules = sum(ram_module.ram_number_of_modules.number_of_modules for ram_module in ram_modules)

        if motherboard and ram_modules.exists():
            if not motherboard_supported_rams:
                issues.append("No RAM support configuration found for the selected motherboard.")
                isValid = False

            if not ram_modules:
                issues.append("No RAM modules selected.")
                isValid = False

            for ram_module in ram_modules:
                # Check if the motherboard supports the RAM type
                if motherboard_supported_rams and not any(ram_module.ram_type == supported_ram.ram_type for supported_ram in motherboard_supported_rams):
                    issues.append(f"The selected RAM is not compatible with the motherboard\nMotherboard supports RAM Type {motherboard_supported_rams[0].ram_type if motherboard_supported_rams else 'N/A'}\nSelected RAM has type {ram_module.ram_type}")
                    isValid = False

                # Check if the motherboard supports the RAM speed
                supported_speeds = [int(speed) for config in motherboard_supported_rams for speed in config.supported_speeds.split(',')]
                if int(ram_module.ram_speed.speed) not in supported_speeds:
                    issues.append(f"The selected RAM speed ({ram_module.ram_speed.speed} MHz) is not supported by the motherboard. Supported speeds are: {supported_speeds}.")
                    isValid = False

            if total_ram_capacity > motherboard.max_memory_capacity:
                issues.append(f"The total RAM capacity ({total_ram_capacity} GB) exceeds the maximum capacity of the motherboard ({motherboard.max_memory_capacity} GB).")
                isValid = False

            if total_ram_modules > int(motherboard.memory_slots):
                issues.append(f"The total number of RAM modules ({total_ram_modules}) exceeds the number of slots on the motherboard ({motherboard.memory_slots}).")
                isValid = False

        else:
            issues.append("No motherboard or RAM modules found in the build.")
            isValid = False

        return isValid, issues


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
        storages = build.storages.all()
        isValid = True
        issues = []

        if motherboard and storages.exists():
            for storage_device in storages:
                '''
                supported_storage_config = SupportedStorageConfiguration.objects.filter(motherboard=motherboard, storage_type=storage_device.type).first()
                if not supported_storage_config:
                    issues.append(f"Storage type {storage_device.type} is not supported by the motherboard.")
                elif storage_device.form_factor not in supported_storage_config.supported_form_factors:
                    issues.append(f"Storage form factor {storage_device.form_factor} is not supported by the motherboard.")
                '''
        return isValid, issues
