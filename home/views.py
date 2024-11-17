from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.db import IntegrityError, transaction
from .models import RAM, CPU, Motherboard, Storage, Build, Profile
from .forms import BuildForm
from .compatibility_service import CompatibilityService
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def index(request):
    """
    Render the index page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the index.html template.
    """
    return render(request, 'index.html')

@login_required
def build(request):
    """
    Render the build page where users can create and manage their builds.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the build.html template with the user's build components.
    """
    profile = request.user.profile

    # Retrieve or create an active Build object for the user's profile
    build, created = Build.objects.get_or_create(
        profile=profile,
        is_active=True,
        defaults={'profile': profile, 'is_active': True}
    )

    # If the build was newly created, save it to generate a primary key (build_id)
    if created:
        build.save()

    # Deactivate other active builds for the profile
    Build.objects.filter(profile=profile, is_active=True).exclude(build_id=build.build_id).update(is_active=False)

    context = {
        'build': build,
        'cpu': build.cpu,
        'motherboard': build.motherboard,
        'ram_modules': build.ram.all(),  # Assuming ram is a ManyToManyField
        'storages': build.storages.all()  # Assuming storages is a ManyToManyField
    }
    return render(request, 'build.html', context)


def part_browser(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('q', '')
    results = []

    # You could add your filtering/search logic here based on the category and query if needed.
    # Example:
    if category == 'CPU':
        results = CPU.objects.filter(name__icontains=query)
    elif category == 'RAM':
        results = RAM.objects.filter(name__icontains=query)
    elif category == 'Motherboard':
        results = Motherboard.objects.filter(name__icontains=query)
    elif category == 'Storage':
        results = Storage.objects.filter(name__icontains=query)
    else:
        # Fetch all components
        results = list(CPU.objects.filter(name__icontains=query)) + \
                  list(RAM.objects.filter(name__icontains=query)) + \
                  list(Motherboard.objects.filter(name__icontains=query)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def pre_built(request):
    """
    Render the pre-built page where users can view pre-built PC configurations.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the pre_built.html template.
    """
    return render(request, 'pre_built.html')

def account_page(request):
    """
    Render the account page where users can manage their account information.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the account_page.html template.
    """
    return render(request, 'account_page.html')

def login_or_register(request):
    """
    Handle user login and registration. Present the login form to the user.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the login.html template with the login form.
    """
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('index')
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

@login_required
def search_pc_parts(request):
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', 'All Categories')
    results = []

    if query:
        try:
            if category == 'All Categories' or category == 'RAM':
                ram_results = RAM.objects.filter(
                    Q(name__icontains=query) |
                    Q(ram_type__type__icontains=query) |
                    Q(ram_speed__speed__icontains=query) |
                    Q(ram_capacity__capacity__icontains=query)
                ).distinct()
                for ram in ram_results:
                    ram.category = 'RAM'
                results.extend(ram_results)

            if category == 'All Categories' or category == 'CPU':
                cpu_results = CPU.objects.filter(
                    Q(name__icontains=query) |
                    Q(manufacturer__name__icontains=query) |
                    Q(microarchitecture__name__icontains=query) |
                    Q(socket_type__name__icontains=query)
                ).distinct()
                for cpu in cpu_results:
                    cpu.category = 'CPU'
                results.extend(cpu_results)

            if category == 'All Categories' or category == 'Motherboard':
                motherboard_results = Motherboard.objects.filter(
                    Q(name__icontains=query) |
                    Q(manufacturer__name__icontains=query) |
                    Q(cpu_socket_type__name__icontains=query) |
                    Q(supported_ram_types__type__icontains=query) |
                    Q(supported_ram_speeds__speed__icontains=query)
                ).distinct()
                for motherboard in motherboard_results:
                    motherboard.category = 'Motherboard'
                results.extend(motherboard_results)

            if category == 'All Categories' or category == 'Storage':
                storage_results = Storage.objects.filter(
                    Q(name__icontains=query) |
                    Q(form_factor__name__icontains=query) |
                    Q(capacity__capacity__icontains=query) |
                    Q(type__type__icontains=query)
                ).distinct()
                for storage in storage_results:
                    storage.category = 'Storage'
                results.extend(storage_results)
        except Exception as e:
            messages.error(request, f"An error occurred during the search: {e}")

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})


def register_view(request):
    """
    Handle user registration.
    """
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, "Registration successful.")
            return redirect('index')  # Redirect to your home page after successful registration
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})

@login_required
def add_to_build(request, part_id, category):
    profile = request.user.profile

    # Retrieve the active build
    build = Build.objects.filter(profile=profile, is_active=True).first()

    if not build:
        messages.error(request, "No active build found. Please create a new build.")
        return redirect('build_page')

    # Add the part to the active build
    if category == 'CPU':
        part = get_object_or_404(CPU, cpu_id=part_id)
        build.cpu = part
    elif category == 'RAM':
        part = get_object_or_404(RAM, ram_id=part_id)
        build.ram.add(part)
    elif category == 'Motherboard':
        part = get_object_or_404(Motherboard, motherboard_id=part_id)
        build.motherboard = part
    elif category == 'Storage':
        part = get_object_or_404(Storage, storage_id=part_id)
        build.storages.add(part)

    build.save()  # Save the changes
    return redirect('build')

@login_required
def remove_from_build(request, category):
    # Get the active build for the user
    build = get_object_or_404(Build, profile__user=request.user, is_active=True)

    # Remove the specified component based on the category
    if category == 'CPU':
        build.cpu = None
    elif category == 'RAM':
        build.ram.clear()  # RAM is Many-to-Many
    elif category == 'Motherboard':
        build.motherboard = None
    elif category == 'Storage':
        build.storages.clear()  # Storage is Many-to-Many

    # Save the build
    build.save()

    return redirect('build')  # Redirect back to the build page

def view_profile(request):
    context = {
        'user' : request.username
    }

    return render(request, 'account_page.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')

@login_required
def save_build(request):
    build_name = request.GET.get("build_name")
    profile = request.user.profile

    if not build_name:
        messages.error(request, "Build name cannot be empty.")
        return redirect('build')

    # Retrieve the active build
    current_build = Build.objects.filter(profile=profile, is_active=True).first()

    if not current_build:
        messages.error(request, "No active build found.")
        return redirect('build')

    # Check for duplicate names
    if Build.objects.filter(profile=profile, name=build_name).exists():
        messages.error(request, f"A build with the name '{build_name}' already exists.")
        return redirect('build')

    # Save components and mark the build as complete
    current_build.name = build_name
    current_build.is_active = False  # Mark build as inactive
    current_build.is_complete = True
    current_build.save()

    # Clear the builder page components
    Build.objects.create(profile=profile, is_active=True)  # Create a new active build
    messages.success(request, f"Build '{build_name}' saved successfully!")
    return redirect('account_page')

@login_required
def delete_build(request, build_id):
    build = get_object_or_404(Build, build_id=build_id, profile__user=request.user)
    build.delete()
    messages.success(request, "Build deleted successfully.")
    return redirect('account_page')


def edit_build(request, build_id):
    build = get_object_or_404(Build, build_id=build_id, profile__user=request.user)

    if request.method == "POST":
        form = BuildForm(request.POST, instance=build)
        if form.is_valid():
            # Save the form first to ensure build_id is generated
            build = form.save(commit=False)
            build.save()  # Save to get a primary key

            # Now set the many-to-many fields
            form.cleaned_data.get('ram') and build.ram.set(form.cleaned_data['ram'])
            form.cleaned_data.get('storages') and build.storages.set(form.cleaned_data['storages'])

            # Check compatibility after saving
            try:
                CompatibilityService.check_build_compatibility(build)
                messages.success(request, "Build saved and is compatible!")
            except ValueError as e:
                messages.error(request, f"Build saved but compatibility issues detected: {e}")
            return redirect('account_page')
    else:
        form = BuildForm(instance=build)

    return render(request, 'edit_build.html', {'form': form})

def view_build(request, build_id):
    build = get_object_or_404(Build, build_id=build_id)
    return render(request, 'view_build.html', {'build': build})