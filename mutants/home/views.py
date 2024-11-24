
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import RAM, CPU, Motherboard, Storage, Build
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def x_logout_view__mutmut_orig(request):
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

def x_logout_view__mutmut_1(request):
    """
    Handle user logout by logging out the user and redirecting to the login page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Redirects to the login_or_register view.
    """
    auth_logout(None)
    messages.success(request, "Logged out successfully.")
    return redirect('login_or_register')

def x_logout_view__mutmut_2(request):
    """
    Handle user logout by logging out the user and redirecting to the login page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Redirects to the login_or_register view.
    """
    auth_logout(request)
    messages.success(None, "Logged out successfully.")
    return redirect('login_or_register')

def x_logout_view__mutmut_3(request):
    """
    Handle user logout by logging out the user and redirecting to the login page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Redirects to the login_or_register view.
    """
    auth_logout(request)
    messages.success(request, "XXLogged out successfully.XX")
    return redirect('login_or_register')

def x_logout_view__mutmut_4(request):
    """
    Handle user logout by logging out the user and redirecting to the login page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Redirects to the login_or_register view.
    """
    auth_logout(request)
    messages.success( "Logged out successfully.")
    return redirect('login_or_register')

def x_logout_view__mutmut_5(request):
    """
    Handle user logout by logging out the user and redirecting to the login page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Redirects to the login_or_register view.
    """
    auth_logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('XXlogin_or_registerXX')

x_logout_view__mutmut_mutants = {
'x_logout_view__mutmut_1': x_logout_view__mutmut_1, 
    'x_logout_view__mutmut_2': x_logout_view__mutmut_2, 
    'x_logout_view__mutmut_3': x_logout_view__mutmut_3, 
    'x_logout_view__mutmut_4': x_logout_view__mutmut_4, 
    'x_logout_view__mutmut_5': x_logout_view__mutmut_5
}

def logout_view(*args, **kwargs):
    result = _mutmut_trampoline(x_logout_view__mutmut_orig, x_logout_view__mutmut_mutants, *args, **kwargs)
    return result 

logout_view.__signature__ = _mutmut_signature(x_logout_view__mutmut_orig)
x_logout_view__mutmut_orig.__name__ = 'x_logout_view'



def x_index__mutmut_orig(request):
    """
    Render the index page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the index.html template.
    """
    return render(request, 'index.html')

def x_index__mutmut_1(request):
    """
    Render the index page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the index.html template.
    """
    return render(None, 'index.html')

def x_index__mutmut_2(request):
    """
    Render the index page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the index.html template.
    """
    return render(request, 'XXindex.htmlXX')

def x_index__mutmut_3(request):
    """
    Render the index page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the index.html template.
    """
    return render( 'index.html')

x_index__mutmut_mutants = {
'x_index__mutmut_1': x_index__mutmut_1, 
    'x_index__mutmut_2': x_index__mutmut_2, 
    'x_index__mutmut_3': x_index__mutmut_3
}

def index(*args, **kwargs):
    result = _mutmut_trampoline(x_index__mutmut_orig, x_index__mutmut_mutants, *args, **kwargs)
    return result 

index.__signature__ = _mutmut_signature(x_index__mutmut_orig)
x_index__mutmut_orig.__name__ = 'x_index'



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

def x_part_browser__mutmut_orig(request):
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

def x_part_browser__mutmut_1(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('XXcategoryXX', 'All Categories')
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

def x_part_browser__mutmut_2(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'XXAll CategoriesXX')
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

def x_part_browser__mutmut_3(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = None
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

def x_part_browser__mutmut_4(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('XXqXX', '')
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

def x_part_browser__mutmut_5(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('q', 'XXXX')
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

def x_part_browser__mutmut_6(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = None
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

def x_part_browser__mutmut_7(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('q', '')
    results = None

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

def x_part_browser__mutmut_8(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('q', '')
    results = []

    # You could add your filtering/search logic here based on the category and query if needed.
    # Example:
    if category != 'CPU':
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

def x_part_browser__mutmut_9(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('q', '')
    results = []

    # You could add your filtering/search logic here based on the category and query if needed.
    # Example:
    if category == 'XXCPUXX':
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

def x_part_browser__mutmut_10(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('q', '')
    results = []

    # You could add your filtering/search logic here based on the category and query if needed.
    # Example:
    if category == 'CPU':
        results = CPU.objects.filter(name__icontains=None)
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

def x_part_browser__mutmut_11(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('q', '')
    results = []

    # You could add your filtering/search logic here based on the category and query if needed.
    # Example:
    if category == 'CPU':
        results = None
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

def x_part_browser__mutmut_12(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('q', '')
    results = []

    # You could add your filtering/search logic here based on the category and query if needed.
    # Example:
    if category == 'CPU':
        results = CPU.objects.filter(name__icontains=query)
    elif category != 'RAM':
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

def x_part_browser__mutmut_13(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('q', '')
    results = []

    # You could add your filtering/search logic here based on the category and query if needed.
    # Example:
    if category == 'CPU':
        results = CPU.objects.filter(name__icontains=query)
    elif category == 'XXRAMXX':
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

def x_part_browser__mutmut_14(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('q', '')
    results = []

    # You could add your filtering/search logic here based on the category and query if needed.
    # Example:
    if category == 'CPU':
        results = CPU.objects.filter(name__icontains=query)
    elif category == 'RAM':
        results = RAM.objects.filter(name__icontains=None)
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

def x_part_browser__mutmut_15(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('q', '')
    results = []

    # You could add your filtering/search logic here based on the category and query if needed.
    # Example:
    if category == 'CPU':
        results = CPU.objects.filter(name__icontains=query)
    elif category == 'RAM':
        results = None
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

def x_part_browser__mutmut_16(request):
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
    elif category != 'Motherboard':
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

def x_part_browser__mutmut_17(request):
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
    elif category == 'XXMotherboardXX':
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

def x_part_browser__mutmut_18(request):
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
        results = Motherboard.objects.filter(name__icontains=None)
    elif category == 'Storage':
        results = Storage.objects.filter(name__icontains=query)
    else:
        # Fetch all components
        results = list(CPU.objects.filter(name__icontains=query)) + \
                  list(RAM.objects.filter(name__icontains=query)) + \
                  list(Motherboard.objects.filter(name__icontains=query)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_19(request):
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
        results = None
    elif category == 'Storage':
        results = Storage.objects.filter(name__icontains=query)
    else:
        # Fetch all components
        results = list(CPU.objects.filter(name__icontains=query)) + \
                  list(RAM.objects.filter(name__icontains=query)) + \
                  list(Motherboard.objects.filter(name__icontains=query)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_20(request):
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
    elif category != 'Storage':
        results = Storage.objects.filter(name__icontains=query)
    else:
        # Fetch all components
        results = list(CPU.objects.filter(name__icontains=query)) + \
                  list(RAM.objects.filter(name__icontains=query)) + \
                  list(Motherboard.objects.filter(name__icontains=query)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_21(request):
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
    elif category == 'XXStorageXX':
        results = Storage.objects.filter(name__icontains=query)
    else:
        # Fetch all components
        results = list(CPU.objects.filter(name__icontains=query)) + \
                  list(RAM.objects.filter(name__icontains=query)) + \
                  list(Motherboard.objects.filter(name__icontains=query)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_22(request):
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
        results = Storage.objects.filter(name__icontains=None)
    else:
        # Fetch all components
        results = list(CPU.objects.filter(name__icontains=query)) + \
                  list(RAM.objects.filter(name__icontains=query)) + \
                  list(Motherboard.objects.filter(name__icontains=query)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_23(request):
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
        results = None
    else:
        # Fetch all components
        results = list(CPU.objects.filter(name__icontains=query)) + \
                  list(RAM.objects.filter(name__icontains=query)) + \
                  list(Motherboard.objects.filter(name__icontains=query)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_24(request):
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
        results = list(CPU.objects.filter(name__icontains=None)) + \
                  list(RAM.objects.filter(name__icontains=query)) + \
                  list(Motherboard.objects.filter(name__icontains=query)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_25(request):
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
        results = list(CPU.objects.filter(name__icontains=query)) - \
                  list(RAM.objects.filter(name__icontains=query)) + \
                  list(Motherboard.objects.filter(name__icontains=query)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_26(request):
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
                  list(RAM.objects.filter(name__icontains=None)) + \
                  list(Motherboard.objects.filter(name__icontains=query)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_27(request):
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
                  list(RAM.objects.filter(name__icontains=query)) - \
                  list(Motherboard.objects.filter(name__icontains=query)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_28(request):
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
                  list(Motherboard.objects.filter(name__icontains=None)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_29(request):
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
                  list(Motherboard.objects.filter(name__icontains=query)) - \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_30(request):
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
                  list(Storage.objects.filter(name__icontains=None))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_31(request):
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
        results = None

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_32(request):
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

    return render(None, 'part_browser.html', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_33(request):
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

    return render(request, 'XXpart_browser.htmlXX', {'results': results, 'query': query, 'category': category})

def x_part_browser__mutmut_34(request):
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

    return render(request, 'part_browser.html', {'XXresultsXX': results, 'query': query, 'category': category})

def x_part_browser__mutmut_35(request):
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

    return render(request, 'part_browser.html', {'results': results, 'XXqueryXX': query, 'category': category})

def x_part_browser__mutmut_36(request):
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

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'XXcategoryXX': category})

def x_part_browser__mutmut_37(request):
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

    return render( 'part_browser.html', {'results': results, 'query': query, 'category': category})

x_part_browser__mutmut_mutants = {
'x_part_browser__mutmut_1': x_part_browser__mutmut_1, 
    'x_part_browser__mutmut_2': x_part_browser__mutmut_2, 
    'x_part_browser__mutmut_3': x_part_browser__mutmut_3, 
    'x_part_browser__mutmut_4': x_part_browser__mutmut_4, 
    'x_part_browser__mutmut_5': x_part_browser__mutmut_5, 
    'x_part_browser__mutmut_6': x_part_browser__mutmut_6, 
    'x_part_browser__mutmut_7': x_part_browser__mutmut_7, 
    'x_part_browser__mutmut_8': x_part_browser__mutmut_8, 
    'x_part_browser__mutmut_9': x_part_browser__mutmut_9, 
    'x_part_browser__mutmut_10': x_part_browser__mutmut_10, 
    'x_part_browser__mutmut_11': x_part_browser__mutmut_11, 
    'x_part_browser__mutmut_12': x_part_browser__mutmut_12, 
    'x_part_browser__mutmut_13': x_part_browser__mutmut_13, 
    'x_part_browser__mutmut_14': x_part_browser__mutmut_14, 
    'x_part_browser__mutmut_15': x_part_browser__mutmut_15, 
    'x_part_browser__mutmut_16': x_part_browser__mutmut_16, 
    'x_part_browser__mutmut_17': x_part_browser__mutmut_17, 
    'x_part_browser__mutmut_18': x_part_browser__mutmut_18, 
    'x_part_browser__mutmut_19': x_part_browser__mutmut_19, 
    'x_part_browser__mutmut_20': x_part_browser__mutmut_20, 
    'x_part_browser__mutmut_21': x_part_browser__mutmut_21, 
    'x_part_browser__mutmut_22': x_part_browser__mutmut_22, 
    'x_part_browser__mutmut_23': x_part_browser__mutmut_23, 
    'x_part_browser__mutmut_24': x_part_browser__mutmut_24, 
    'x_part_browser__mutmut_25': x_part_browser__mutmut_25, 
    'x_part_browser__mutmut_26': x_part_browser__mutmut_26, 
    'x_part_browser__mutmut_27': x_part_browser__mutmut_27, 
    'x_part_browser__mutmut_28': x_part_browser__mutmut_28, 
    'x_part_browser__mutmut_29': x_part_browser__mutmut_29, 
    'x_part_browser__mutmut_30': x_part_browser__mutmut_30, 
    'x_part_browser__mutmut_31': x_part_browser__mutmut_31, 
    'x_part_browser__mutmut_32': x_part_browser__mutmut_32, 
    'x_part_browser__mutmut_33': x_part_browser__mutmut_33, 
    'x_part_browser__mutmut_34': x_part_browser__mutmut_34, 
    'x_part_browser__mutmut_35': x_part_browser__mutmut_35, 
    'x_part_browser__mutmut_36': x_part_browser__mutmut_36, 
    'x_part_browser__mutmut_37': x_part_browser__mutmut_37
}

def part_browser(*args, **kwargs):
    result = _mutmut_trampoline(x_part_browser__mutmut_orig, x_part_browser__mutmut_mutants, *args, **kwargs)
    return result 

part_browser.__signature__ = _mutmut_signature(x_part_browser__mutmut_orig)
x_part_browser__mutmut_orig.__name__ = 'x_part_browser'



def x_pre_built__mutmut_orig(request):
    """
    Render the pre-built page where users can view pre-built PC configurations.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the pre_built.html template.
    """
    return render(request, 'pre_built.html')

def x_pre_built__mutmut_1(request):
    """
    Render the pre-built page where users can view pre-built PC configurations.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the pre_built.html template.
    """
    return render(None, 'pre_built.html')

def x_pre_built__mutmut_2(request):
    """
    Render the pre-built page where users can view pre-built PC configurations.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the pre_built.html template.
    """
    return render(request, 'XXpre_built.htmlXX')

def x_pre_built__mutmut_3(request):
    """
    Render the pre-built page where users can view pre-built PC configurations.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the pre_built.html template.
    """
    return render( 'pre_built.html')

x_pre_built__mutmut_mutants = {
'x_pre_built__mutmut_1': x_pre_built__mutmut_1, 
    'x_pre_built__mutmut_2': x_pre_built__mutmut_2, 
    'x_pre_built__mutmut_3': x_pre_built__mutmut_3
}

def pre_built(*args, **kwargs):
    result = _mutmut_trampoline(x_pre_built__mutmut_orig, x_pre_built__mutmut_mutants, *args, **kwargs)
    return result 

pre_built.__signature__ = _mutmut_signature(x_pre_built__mutmut_orig)
x_pre_built__mutmut_orig.__name__ = 'x_pre_built'



def x_account_page__mutmut_orig(request):
    """
    Render the account page where users can manage their account information.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the account_page.html template.
    """
    return render(request, 'account_page.html')

def x_account_page__mutmut_1(request):
    """
    Render the account page where users can manage their account information.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the account_page.html template.
    """
    return render(None, 'account_page.html')

def x_account_page__mutmut_2(request):
    """
    Render the account page where users can manage their account information.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the account_page.html template.
    """
    return render(request, 'XXaccount_page.htmlXX')

def x_account_page__mutmut_3(request):
    """
    Render the account page where users can manage their account information.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the account_page.html template.
    """
    return render( 'account_page.html')

x_account_page__mutmut_mutants = {
'x_account_page__mutmut_1': x_account_page__mutmut_1, 
    'x_account_page__mutmut_2': x_account_page__mutmut_2, 
    'x_account_page__mutmut_3': x_account_page__mutmut_3
}

def account_page(*args, **kwargs):
    result = _mutmut_trampoline(x_account_page__mutmut_orig, x_account_page__mutmut_mutants, *args, **kwargs)
    return result 

account_page.__signature__ = _mutmut_signature(x_account_page__mutmut_orig)
x_account_page__mutmut_orig.__name__ = 'x_account_page'



def x_login_or_register__mutmut_orig(request):
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

def x_login_or_register__mutmut_1(request):
    """
    Handle user login and registration. Present the login form to the user.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the login.html template with the login form.
    """
    if request.method != 'POST':
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

def x_login_or_register__mutmut_2(request):
    """
    Handle user login and registration. Present the login form to the user.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the login.html template with the login form.
    """
    if request.method == 'XXPOSTXX':
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

def x_login_or_register__mutmut_3(request):
    """
    Handle user login and registration. Present the login form to the user.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the login.html template with the login form.
    """
    if request.method == 'POST':
        login_form = AuthenticationForm(None, data=request.POST)
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

def x_login_or_register__mutmut_4(request):
    """
    Handle user login and registration. Present the login form to the user.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the login.html template with the login form.
    """
    if request.method == 'POST':
        login_form = AuthenticationForm( data=request.POST)
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

def x_login_or_register__mutmut_5(request):
    """
    Handle user login and registration. Present the login form to the user.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the login.html template with the login form.
    """
    if request.method == 'POST':
        login_form = AuthenticationForm(request,)
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

def x_login_or_register__mutmut_6(request):
    """
    Handle user login and registration. Present the login form to the user.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the login.html template with the login form.
    """
    if request.method == 'POST':
        login_form = None
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

def x_login_or_register__mutmut_7(request):
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
            username = login_form.cleaned_data.get('XXusernameXX')
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

def x_login_or_register__mutmut_8(request):
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
            username = None
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

def x_login_or_register__mutmut_9(request):
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
            password = login_form.cleaned_data.get('XXpasswordXX')
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

def x_login_or_register__mutmut_10(request):
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
            password = None
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

def x_login_or_register__mutmut_11(request):
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
            user = authenticate(username=None, password=password)
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

def x_login_or_register__mutmut_12(request):
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
            user = authenticate(username=username, password=None)
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

def x_login_or_register__mutmut_13(request):
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
            user = authenticate( password=password)
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

def x_login_or_register__mutmut_14(request):
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
            user = authenticate(username=username,)
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

def x_login_or_register__mutmut_15(request):
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
            user = None
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

def x_login_or_register__mutmut_16(request):
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
            if user is  None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('index')
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_17(request):
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
                login(None, user)
                messages.success(request, "Login successful.")
                return redirect('index')
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_18(request):
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
                login(request, None)
                messages.success(request, "Login successful.")
                return redirect('index')
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_19(request):
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
                login( user)
                messages.success(request, "Login successful.")
                return redirect('index')
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_20(request):
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
                login(request,)
                messages.success(request, "Login successful.")
                return redirect('index')
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_21(request):
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
                messages.success(None, "Login successful.")
                return redirect('index')
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_22(request):
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
                messages.success(request, "XXLogin successful.XX")
                return redirect('index')
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_23(request):
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
                messages.success( "Login successful.")
                return redirect('index')
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_24(request):
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
                return redirect('XXindexXX')
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_25(request):
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
                messages.error(None, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_26(request):
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
                messages.error(request, "XXInvalid login credentials.XX")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_27(request):
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
                messages.error( "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_28(request):
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
            messages.error(None, "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_29(request):
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
            messages.error(request, "XXInvalid login form submission.XX")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_30(request):
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
            messages.error( "Invalid login form submission.")
    
    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_31(request):
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
    
    login_form = None
    return render(request, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_32(request):
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
    return render(None, 'auth/login.html', {'login_form': login_form})

def x_login_or_register__mutmut_33(request):
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
    return render(request, 'XXauth/login.htmlXX', {'login_form': login_form})

def x_login_or_register__mutmut_34(request):
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
    return render(request, 'auth/login.html', {'XXlogin_formXX': login_form})

def x_login_or_register__mutmut_35(request):
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
    return render( 'auth/login.html', {'login_form': login_form})

x_login_or_register__mutmut_mutants = {
'x_login_or_register__mutmut_1': x_login_or_register__mutmut_1, 
    'x_login_or_register__mutmut_2': x_login_or_register__mutmut_2, 
    'x_login_or_register__mutmut_3': x_login_or_register__mutmut_3, 
    'x_login_or_register__mutmut_4': x_login_or_register__mutmut_4, 
    'x_login_or_register__mutmut_5': x_login_or_register__mutmut_5, 
    'x_login_or_register__mutmut_6': x_login_or_register__mutmut_6, 
    'x_login_or_register__mutmut_7': x_login_or_register__mutmut_7, 
    'x_login_or_register__mutmut_8': x_login_or_register__mutmut_8, 
    'x_login_or_register__mutmut_9': x_login_or_register__mutmut_9, 
    'x_login_or_register__mutmut_10': x_login_or_register__mutmut_10, 
    'x_login_or_register__mutmut_11': x_login_or_register__mutmut_11, 
    'x_login_or_register__mutmut_12': x_login_or_register__mutmut_12, 
    'x_login_or_register__mutmut_13': x_login_or_register__mutmut_13, 
    'x_login_or_register__mutmut_14': x_login_or_register__mutmut_14, 
    'x_login_or_register__mutmut_15': x_login_or_register__mutmut_15, 
    'x_login_or_register__mutmut_16': x_login_or_register__mutmut_16, 
    'x_login_or_register__mutmut_17': x_login_or_register__mutmut_17, 
    'x_login_or_register__mutmut_18': x_login_or_register__mutmut_18, 
    'x_login_or_register__mutmut_19': x_login_or_register__mutmut_19, 
    'x_login_or_register__mutmut_20': x_login_or_register__mutmut_20, 
    'x_login_or_register__mutmut_21': x_login_or_register__mutmut_21, 
    'x_login_or_register__mutmut_22': x_login_or_register__mutmut_22, 
    'x_login_or_register__mutmut_23': x_login_or_register__mutmut_23, 
    'x_login_or_register__mutmut_24': x_login_or_register__mutmut_24, 
    'x_login_or_register__mutmut_25': x_login_or_register__mutmut_25, 
    'x_login_or_register__mutmut_26': x_login_or_register__mutmut_26, 
    'x_login_or_register__mutmut_27': x_login_or_register__mutmut_27, 
    'x_login_or_register__mutmut_28': x_login_or_register__mutmut_28, 
    'x_login_or_register__mutmut_29': x_login_or_register__mutmut_29, 
    'x_login_or_register__mutmut_30': x_login_or_register__mutmut_30, 
    'x_login_or_register__mutmut_31': x_login_or_register__mutmut_31, 
    'x_login_or_register__mutmut_32': x_login_or_register__mutmut_32, 
    'x_login_or_register__mutmut_33': x_login_or_register__mutmut_33, 
    'x_login_or_register__mutmut_34': x_login_or_register__mutmut_34, 
    'x_login_or_register__mutmut_35': x_login_or_register__mutmut_35
}

def login_or_register(*args, **kwargs):
    result = _mutmut_trampoline(x_login_or_register__mutmut_orig, x_login_or_register__mutmut_mutants, *args, **kwargs)
    return result 

login_or_register.__signature__ = _mutmut_signature(x_login_or_register__mutmut_orig)
x_login_or_register__mutmut_orig.__name__ = 'x_login_or_register'



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


def x_register_view__mutmut_orig(request):
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


def x_register_view__mutmut_1(request):
    """
    Handle user registration by creating a new user and logging them in.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the register.html template with the registration form.
    """
    if request.method != 'POST':
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


def x_register_view__mutmut_2(request):
    """
    Handle user registration by creating a new user and logging them in.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the register.html template with the registration form.
    """
    if request.method == 'XXPOSTXX':
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


def x_register_view__mutmut_3(request):
    """
    Handle user registration by creating a new user and logging them in.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the register.html template with the registration form.
    """
    if request.method == 'POST':
        register_form = None
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


def x_register_view__mutmut_4(request):
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
            user = None
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_5(request):
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
            login(None, user)
            messages.success(request, "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_6(request):
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
            login(request, None)
            messages.success(request, "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_7(request):
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
            login( user)
            messages.success(request, "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_8(request):
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
            login(request,)
            messages.success(request, "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_9(request):
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
            messages.success(None, "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_10(request):
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
            messages.success(request, "XXRegistration successful.XX")
            return redirect('index')
        else:
            messages.error(request, "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_11(request):
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
            messages.success( "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_12(request):
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
            return redirect('XXindexXX')
        else:
            messages.error(request, "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_13(request):
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
            messages.error(None, "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_14(request):
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
            messages.error(request, "XXRegistration failed.XX")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_15(request):
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
            messages.error( "Registration failed.")
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_16(request):
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
        register_form = None

    return render(request, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_17(request):
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

    return render(None, 'auth/register.html', {'register_form': register_form})


def x_register_view__mutmut_18(request):
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

    return render(request, 'XXauth/register.htmlXX', {'register_form': register_form})


def x_register_view__mutmut_19(request):
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

    return render(request, 'auth/register.html', {'XXregister_formXX': register_form})


def x_register_view__mutmut_20(request):
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

    return render( 'auth/register.html', {'register_form': register_form})

x_register_view__mutmut_mutants = {
'x_register_view__mutmut_1': x_register_view__mutmut_1, 
    'x_register_view__mutmut_2': x_register_view__mutmut_2, 
    'x_register_view__mutmut_3': x_register_view__mutmut_3, 
    'x_register_view__mutmut_4': x_register_view__mutmut_4, 
    'x_register_view__mutmut_5': x_register_view__mutmut_5, 
    'x_register_view__mutmut_6': x_register_view__mutmut_6, 
    'x_register_view__mutmut_7': x_register_view__mutmut_7, 
    'x_register_view__mutmut_8': x_register_view__mutmut_8, 
    'x_register_view__mutmut_9': x_register_view__mutmut_9, 
    'x_register_view__mutmut_10': x_register_view__mutmut_10, 
    'x_register_view__mutmut_11': x_register_view__mutmut_11, 
    'x_register_view__mutmut_12': x_register_view__mutmut_12, 
    'x_register_view__mutmut_13': x_register_view__mutmut_13, 
    'x_register_view__mutmut_14': x_register_view__mutmut_14, 
    'x_register_view__mutmut_15': x_register_view__mutmut_15, 
    'x_register_view__mutmut_16': x_register_view__mutmut_16, 
    'x_register_view__mutmut_17': x_register_view__mutmut_17, 
    'x_register_view__mutmut_18': x_register_view__mutmut_18, 
    'x_register_view__mutmut_19': x_register_view__mutmut_19, 
    'x_register_view__mutmut_20': x_register_view__mutmut_20
}

def register_view(*args, **kwargs):
    result = _mutmut_trampoline(x_register_view__mutmut_orig, x_register_view__mutmut_mutants, *args, **kwargs)
    return result 

register_view.__signature__ = _mutmut_signature(x_register_view__mutmut_orig)
x_register_view__mutmut_orig.__name__ = 'x_register_view'



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
