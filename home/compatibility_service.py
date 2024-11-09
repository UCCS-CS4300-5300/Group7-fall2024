# compatibility_service.py

class CompatibilityService:

    @staticmethod
    def check_build_compatibility(build):
        CompatibilityService.check_cpu_compatibility(build)
        CompatibilityService.check_ram_compatibility(build)
        CompatibilityService.check_storage_compatibility(build)

    @staticmethod
    def check_cpu_compatibility(build):
        motherboard = build.motherboard
        cpu = build.cpu
        if motherboard and cpu:
            if motherboard.cpu_socket_type != cpu.socket_type:
                raise ValueError("The selected CPU is not compatible with the motherboard.")

    @staticmethod
    def check_ram_compatibility(build):
        motherboard = build.motherboard
        ram_modules = build.ram.all()

        def parse_capacity(ram_capacity):
            return int(ram_capacity.rstrip('GB'))

        total_ram_capacity = sum(parse_capacity(ram_module.ram_capacity.capacity) for ram_module in ram_modules)
        total_ram_modules = sum(int(ram_module.ram_number_of_modules.number_of_modules) for ram_module in ram_modules)

        if motherboard and ram_modules.exists():
            for ram_module in ram_modules:
                if ram_module.ram_type not in motherboard.supported_ram_types.all():
                    raise ValueError(f"RAM type {ram_module.ram_type} is not supported by the motherboard {motherboard.name}.")
            if total_ram_capacity > int(motherboard.max_memory_capacity):
                raise ValueError(f"The total RAM capacity ({total_ram_capacity} GB) exceeds the maximum capacity of the motherboard ({motherboard.max_memory_capacity} GB).")
            if total_ram_modules > int(motherboard.memory_slots):
                raise ValueError(f"The total number of RAM modules ({total_ram_modules}) exceeds the number of slots on the motherboard ({motherboard.memory_slots}).")

    @staticmethod
    def check_storage_compatibility(build):
        motherboard = build.motherboard
        storage = build.storage
        if motherboard and storage:
            if storage.storage_type not in motherboard.supported_storage_types.all() or \
            storage.storage_form_factor not in motherboard.storage_form_factor.all():
                raise ValueError("The selected storage is not compatible with the motherboard.")
