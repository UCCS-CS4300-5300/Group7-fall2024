from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import RAM, CPU, Motherboard, Storage
from django.db.models import Q
from rest_framework import viewsets
from .models import Build
from .serializers import BuildSerializer

class BuildViewSet(viewsets.ModelViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer

def index(request):
    return render(request, 'index.html')
# Create your views here.
def build(request):
    return render(request, 'build.html')

def part_browser(request):
    return render(request, 'part_browser.html')

def pre_built(request):
    return render(request, 'pre_built.html')

def login_or_register(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            # Handle user registration
            register_form = UserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)  # Log the user in after registration
                messages.success(request, "Registration successful.")
                return redirect('index')  # Redirect to your desired page
        else:
            # Handle user login
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login successful.")
                    return redirect('index')  # Redirect to your desired page
            else:
                messages.error(request, "Invalid login credentials.")

    # Display both forms when it's a GET request
    login_form = AuthenticationForm()
    register_form = UserCreationForm()
    return render(request, 'auth/login_or_register.html', {
        'login_form': login_form,
        'register_form': register_form
    })

def search_pc_parts(request):
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', 'All Categories')

    results = []

    if query:
        # Perform search based on the category
        if category == 'All Categories' or category == 'RAM':
            if query.lower() == "ram":  # General term to match all RAM entries
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

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

