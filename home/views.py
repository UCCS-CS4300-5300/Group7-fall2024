from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import RAM, CPU, Motherboard, Storage, Build
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def logout_view(request):
    """
    Handle user logout by logging out the user and redirecting to the login page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Redirects to the login_or_register view.
    """
    auth_logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login_or_register')

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
    # Retrieve or create a Build object for the current user's profile
    build, created = Build.objects.get_or_create(profile__user=request.user, defaults={'profile': request.user.profile})

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
    # Ensure the user has a Build object; if not, create one
    build, created = Build.objects.get_or_create(profile__user=request.user, defaults={'profile': request.user.profile})

    # Retrieve the part based on the category and add it to the build
    if category == 'CPU':
        part = get_object_or_404(CPU, cpu_id=part_id)
        build.cpu = part
    elif category == 'RAM':
        part = get_object_or_404(RAM, ram_id=part_id)
        build.ram.add(part)  # Assuming RAM can have multiple items
    elif category == 'Motherboard':
        part = get_object_or_404(Motherboard, motherboard_id=part_id)
        build.motherboard = part
    elif category == 'Storage':
        part = get_object_or_404(Storage, storage_id=part_id)
        build.storages.add(part)  # Assuming Storage is also a ManyToManyField in the build model

    # Save the build after modifications
    build.save()
    return redirect('build')  # Redirect to the build page after adding

@login_required
def remove_from_build(request, category):
    # Get the user's build based on their profile
    build = get_object_or_404(Build, profile__user=request.user)

    # Clear the specified component based on the category
    if category == 'CPU':
        build.cpu = None
    elif category == 'RAM':
        build.ram.clear()  # Assuming RAM is a ManyToManyField
    elif category == 'Motherboard':
        build.motherboard = None
    elif category == 'Storage':
        build.storages.clear()  # Assuming Storage is a ManyToManyField
    # Add similar conditions for other components like GPU, Case, etc.

    # Save the build after removing the component
    build.save()

    # Redirect to the build page after removal
    return redirect('build')

def view_profile(request):
    context = {
        'user' : request.username
    }

    return render(request, 'account_page.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')