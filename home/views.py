from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import RAM, CPU, Motherboard, Storage
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def index(request):
    """
    Render the index page.
    """
    return render(request, 'index.html')

def build(request):
    """
    Render the build page.
    """
    return render(request, 'build.html')

def part_browser(request):
    """
    Render the part browser page.
    """
    return render(request, 'part_browser.html')

def pre_built(request):
    """
    Render the pre-built page.
    """
    return render(request, 'pre_built.html')

def account_page(request):
    """
    Render the pre-built page.
    """
    return render(request, 'account_page.html')

def login_or_register(request):
    """
    Handle user login and registration.
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
    Search for PC parts based on query and category.
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
                        Q(cpu_name__icontains=query) |
                        Q(cpu_manufacturer__name__icontains=query) |
                        Q(cpu_microarchitecture__name__icontains=query) |
                        Q(socket_type__name__icontains=query)
                    ).distinct())

            if category == 'All Categories' or category == 'Motherboard':
                if query.lower() == "motherboard":
                    results += list(Motherboard.objects.all())
                else:
                    results += list(Motherboard.objects.filter(
                        Q(name__icontains=query) |
                        Q(motherboard_manufacturer__name__icontains=query) |
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
                        Q(storage_form_factor__name__icontains=query) |
                        Q(storage_capacity__capacity__icontains=query) |
                        Q(storage_type__type__icontains=query)
                    ).distinct())
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
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})
