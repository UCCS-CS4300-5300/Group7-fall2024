from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import RAM, CPU, Motherboard, Storage
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

def build(request):
    """
    Render the build page where users can create and manage their builds.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the build.html template.
    """
    return render(request, 'build.html')

def part_browser(request):
    """
    Render the part browser page where users can browse various PC parts.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the part_browser.html template.
    """
    return render(request, 'part_browser.html')

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
    """
    Search for PC parts based on the user's query and category selection.
    
    Args:
        request (HttpRequest): The HTTP request object containing the query and category.
        
    Returns:
        HttpResponse: Renders the part_browser.html template with search results.
    """
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', 'All Categories')

    results = []

    if query:
        try:
            if category == 'All Categories' or category == 'RAM':
                if query.lower() == "ram":
                    results += list(RAM.objects.all())
                else:
                    results += list(RAM.objects.filter(
                        Q(ram_type__type__icontains=query) |
                        Q(ram_speed__speed__icontains=query) |
                        Q(ram_capacity__capacity__icontains=query)
                    ).distinct())

            if category == 'All Categories' or category == 'CPU':
                if query.lower() == "cpu":
                    results += list(CPU.objects.all())
                else:
                    results += list(CPU.objects.filter(
                        Q(name__icontains=query) |
                        Q(manufacturer__name__icontains=query) |
                        Q(microarchitecture__name__icontains=query) |
                        Q(socket_type__name__icontains=query)
                    ).distinct())

            if category == 'All Categories' or category == 'Motherboard':
                if query.lower() == "motherboard":
                    results += list(Motherboard.objects.all())
                else:
                    results += list(Motherboard.objects.filter(
                        Q(name__icontains=query) |
                        Q(manufacturer__name__icontains=query) |
                        Q(cpu_socket_type__name__icontains=query) |
                        Q(supported_ram_types__type__icontains=query) |
                        Q(supported_ram_speeds__speed__icontains=query)
                    ).distinct())

            if category == 'All Categories' or category == 'Storage':
                if query.lower() == "storage":
                    results += list(Storage.objects.all())
                else:
                    results += list(Storage.objects.filter(
                        Q(name__icontains=query) |
                        Q(form_factor__name__icontains=query) |
                        Q(capacity__capacity__icontains=query) |
                        Q(type__type__icontains=query)
                    ).distinct())
        except Exception as e:
            messages.error(request, f"An error occurred during the search: {e}")

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def register_view(request):
    """
    Handle user registration by creating a new user and logging them in.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the register.html template with the registration form.
    """
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})
