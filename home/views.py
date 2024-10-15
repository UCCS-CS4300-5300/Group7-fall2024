from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

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
