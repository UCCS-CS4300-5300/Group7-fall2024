# API Search Endpoints

- **Change Username**
  ...app-{devedu-username}-5.io...

## Motherboards
- **Search for motherboards that support a specific RAM type (e.g., DDR5):**
  http://app-dbuck3-5.devedu.io/api/search/motherboards/?ram_type=DDR5

- **Search for motherboards by manufacturer (e.g., ASUS):**
  http://app-dbuck3-5.devedu.io/api/search/motherboards/?manufacturer=ASUS

- **Search for motherboards by CPU socket type (e.g., AM4):**
  http://app-dbuck3-5.devedu.io/api/search/motherboards/?socket_type=AM4

- **Search for motherboards with a specific number of memory slots (e.g., 4 slots):**
  http://app-dbuck3-5.devedu.io/api/search/motherboards/?memory_slots=4

- **Search for motherboards by storage form factor (e.g., M.2):**
  http://app-dbuck3-5.devedu.io/api/search/motherboards/?storage_form_factor=M.2

- **Search for motherboards by maximum memory capacity (e.g., 128GB):**
  http://app-dbuck3-5.devedu.io/api/search/motherboards/?max_memory_capacity=128

## CPUs
- **Search for CPUs with a specific socket type (e.g., AM4):**
  http://app-dbuck3-5.devedu.io/api/search/cpus/?socket_type=AM4

- **Search for CPUs by manufacturer (e.g., Intel):**
  http://app-dbuck3-5.devedu.io/api/search/cpus/?manufacturer=Intel

- **Search for CPUs by microarchitecture (e.g., Skylake):**
  http://app-dbuck3-5.devedu.io/api/search/cpus/?microarchitecture=Skylake

## RAM
- **Search for RAMs with a specific memory type (e.g., DDR4):**
  http://app-dbuck3-5.devedu.io/api/search/rams/?memory_type=DDR4

- **Search for RAMs by speed (e.g., 3200MHz):**
  http://app-dbuck3-5.devedu.io/api/search/rams/?speed=3200MHz

- **Search for RAMs by capacity (e.g., 16GB):**
  http://app-dbuck3-5.devedu.io/api/search/rams/?capacity=16GB

- **Search for RAMs by number of modules (e.g., 2 modules):**
  http://app-dbuck3-5.devedu.io/api/search/rams/?number_of_modules=2

- **Search for RAMs by manufacturer (e.g., Corsair):**
  http://app-dbuck3-5.devedu.io/api/search/rams/?manufacturer=Corsair

## Storages
- **Search for storages with a specific storage type (e.g., SSD):**
  http://app-dbuck3-5.devedu.io/api/search/storages/?storage_type=SSD

- **Search for storages by form factor (e.g., 2.5"):**
  http://app-dbuck3-5.devedu.io/api/search/storages/?form_factor=2.5

- **Search for storages by capacity (e.g., 1TB):**
  http://app-dbuck3-5.devedu.io/api/search/storages/?capacity=1TB

## Builds
- **Search for all builds:**
  http://app-dbuck3-5.devedu.io/api/builds/

- **Search for builds for a specific user (replace `<user_id>` with the actual user ID):**
  http://app-dbuck3-5.devedu.io/api/user_builds/<user_id>/

- **Search for completed builds:**
  http://app-dbuck3-5.devedu.io/api/builds/?is_complete=true

- **Search for builds by name (e.g., 'Gaming Rig'):**
  http://app-dbuck3-5.devedu.io/api/builds/?name=Gaming%20Rig

- **Search for builds by creation date range (e.g., built in 2023):**
  http://app-dbuck3-5.devedu.io/api/builds/?start_date=2023-01-01&end_date=2023-12-31

## Generic Object Retrieval
- **Get all motherboards:**
  http://app-dbuck3-5.devedu.io/api/motherboards/

- **Get all CPUs:**
  http://app-dbuck3-5.devedu.io/api/cpus/

- **Get all RAMs:**
  http://app-dbuck3-5.devedu.io/api/rams/

- **Get all storages:**
  http://app-dbuck3-5.devedu.io/api/storages/

- **Get all builds:**
  http://app-dbuck3-5.devedu.io/api/builds/
