
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


import requests
from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

def x_fetch_api_data__mutmut_orig(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        context = {'data': result.json()}
        return render(None, template_name, context)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=500)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=500)

def x_fetch_api_data__mutmut_1(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(None)
        result.raise_for_status()
        context = {'data': result.json()}
        return render(None, template_name, context)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=500)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=500)

def x_fetch_api_data__mutmut_2(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = None
        result.raise_for_status()
        context = {'data': result.json()}
        return render(None, template_name, context)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=500)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=500)

def x_fetch_api_data__mutmut_3(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        context = {'XXdataXX': result.json()}
        return render(None, template_name, context)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=500)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=500)

def x_fetch_api_data__mutmut_4(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        context = None
        return render(None, template_name, context)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=500)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=500)

def x_fetch_api_data__mutmut_5(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        context = {'data': result.json()}
        return render(None, None, context)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=500)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=500)

def x_fetch_api_data__mutmut_6(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        context = {'data': result.json()}
        return render(None, template_name, None)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=500)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=500)

def x_fetch_api_data__mutmut_7(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        context = {'data': result.json()}
        return render(None, context)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=500)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=500)

def x_fetch_api_data__mutmut_8(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        context = {'data': result.json()}
        return render(None, template_name,)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=500)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=500)

def x_fetch_api_data__mutmut_9(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        context = {'data': result.json()}
        return render(None, template_name, context)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}",)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=500)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=500)

def x_fetch_api_data__mutmut_10(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        context = {'data': result.json()}
        return render(None, template_name, context)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=501)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=500)

def x_fetch_api_data__mutmut_11(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        context = {'data': result.json()}
        return render(None, template_name, context)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}",)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=500)

def x_fetch_api_data__mutmut_12(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        context = {'data': result.json()}
        return render(None, template_name, context)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=500)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}", status=501)

def x_fetch_api_data__mutmut_13(url, template_name):
    """
    Fetch data from the API and render the specified template with the context.

    Args:
        url (str): The API endpoint URL.
        template_name (str): The name of the template to render.

    Returns:
        HttpResponse: The rendered template or an error message.
    """
    try:
        result = requests.get(url)
        result.raise_for_status()
        context = {'data': result.json()}
        return render(None, template_name, context)
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f"HTTP error occurred: {http_err}", status=result.status_code)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f"Request error occurred: {req_err}", status=500)
    except Exception as err:
        return HttpResponse(f"An unexpected error occurred: {err}",)

x_fetch_api_data__mutmut_mutants = {
'x_fetch_api_data__mutmut_1': x_fetch_api_data__mutmut_1, 
    'x_fetch_api_data__mutmut_2': x_fetch_api_data__mutmut_2, 
    'x_fetch_api_data__mutmut_3': x_fetch_api_data__mutmut_3, 
    'x_fetch_api_data__mutmut_4': x_fetch_api_data__mutmut_4, 
    'x_fetch_api_data__mutmut_5': x_fetch_api_data__mutmut_5, 
    'x_fetch_api_data__mutmut_6': x_fetch_api_data__mutmut_6, 
    'x_fetch_api_data__mutmut_7': x_fetch_api_data__mutmut_7, 
    'x_fetch_api_data__mutmut_8': x_fetch_api_data__mutmut_8, 
    'x_fetch_api_data__mutmut_9': x_fetch_api_data__mutmut_9, 
    'x_fetch_api_data__mutmut_10': x_fetch_api_data__mutmut_10, 
    'x_fetch_api_data__mutmut_11': x_fetch_api_data__mutmut_11, 
    'x_fetch_api_data__mutmut_12': x_fetch_api_data__mutmut_12, 
    'x_fetch_api_data__mutmut_13': x_fetch_api_data__mutmut_13
}

def fetch_api_data(*args, **kwargs):
    result = _mutmut_trampoline(x_fetch_api_data__mutmut_orig, x_fetch_api_data__mutmut_mutants, *args, **kwargs)
    return result 

fetch_api_data.__signature__ = _mutmut_signature(x_fetch_api_data__mutmut_orig)
x_fetch_api_data__mutmut_orig.__name__ = 'x_fetch_api_data'



def x_render_with_api_data__mutmut_orig(api_endpoint, template_name):
    """
    Generic function to render a template with data fetched from the API.

    Args:
        api_endpoint (str): The API endpoint to fetch data from.
        template_name (str): The name of the template to render.

    Returns:
        function: A view function that renders the specified template.
    """
    @login_required(login_url='login/')
    def view_function(request):
        try:
            url = settings.BASE_API_URL.format(settings.CONTAINER_USERNAME) + api_endpoint
            return fetch_api_data(url, template_name)
        except Exception as e:
            return HttpResponse(f"An error occurred while fetching data: {e}", status=500)
    return view_function

def x_render_with_api_data__mutmut_1(api_endpoint, template_name):
    """
    Generic function to render a template with data fetched from the API.

    Args:
        api_endpoint (str): The API endpoint to fetch data from.
        template_name (str): The name of the template to render.

    Returns:
        function: A view function that renders the specified template.
    """
    @login_required(login_url='XXlogin/XX')
    def view_function(request):
        try:
            url = settings.BASE_API_URL.format(settings.CONTAINER_USERNAME) + api_endpoint
            return fetch_api_data(url, template_name)
        except Exception as e:
            return HttpResponse(f"An error occurred while fetching data: {e}", status=500)
    return view_function

def x_render_with_api_data__mutmut_2(api_endpoint, template_name):
    """
    Generic function to render a template with data fetched from the API.

    Args:
        api_endpoint (str): The API endpoint to fetch data from.
        template_name (str): The name of the template to render.

    Returns:
        function: A view function that renders the specified template.
    """

    def view_function(request):
        try:
            url = settings.BASE_API_URL.format(settings.CONTAINER_USERNAME) + api_endpoint
            return fetch_api_data(url, template_name)
        except Exception as e:
            return HttpResponse(f"An error occurred while fetching data: {e}", status=500)
    return view_function

def x_render_with_api_data__mutmut_3(api_endpoint, template_name):
    """
    Generic function to render a template with data fetched from the API.

    Args:
        api_endpoint (str): The API endpoint to fetch data from.
        template_name (str): The name of the template to render.

    Returns:
        function: A view function that renders the specified template.
    """
    @login_required(login_url='login/')
    def view_function(request):
        try:
            url = settings.BASE_API_URL.format(settings.CONTAINER_USERNAME) - api_endpoint
            return fetch_api_data(url, template_name)
        except Exception as e:
            return HttpResponse(f"An error occurred while fetching data: {e}", status=500)
    return view_function

def x_render_with_api_data__mutmut_4(api_endpoint, template_name):
    """
    Generic function to render a template with data fetched from the API.

    Args:
        api_endpoint (str): The API endpoint to fetch data from.
        template_name (str): The name of the template to render.

    Returns:
        function: A view function that renders the specified template.
    """
    @login_required(login_url='login/')
    def view_function(request):
        try:
            url = None
            return fetch_api_data(url, template_name)
        except Exception as e:
            return HttpResponse(f"An error occurred while fetching data: {e}", status=500)
    return view_function

def x_render_with_api_data__mutmut_5(api_endpoint, template_name):
    """
    Generic function to render a template with data fetched from the API.

    Args:
        api_endpoint (str): The API endpoint to fetch data from.
        template_name (str): The name of the template to render.

    Returns:
        function: A view function that renders the specified template.
    """
    @login_required(login_url='login/')
    def view_function(request):
        try:
            url = settings.BASE_API_URL.format(settings.CONTAINER_USERNAME) + api_endpoint
            return fetch_api_data(None, template_name)
        except Exception as e:
            return HttpResponse(f"An error occurred while fetching data: {e}", status=500)
    return view_function

def x_render_with_api_data__mutmut_6(api_endpoint, template_name):
    """
    Generic function to render a template with data fetched from the API.

    Args:
        api_endpoint (str): The API endpoint to fetch data from.
        template_name (str): The name of the template to render.

    Returns:
        function: A view function that renders the specified template.
    """
    @login_required(login_url='login/')
    def view_function(request):
        try:
            url = settings.BASE_API_URL.format(settings.CONTAINER_USERNAME) + api_endpoint
            return fetch_api_data(url, None)
        except Exception as e:
            return HttpResponse(f"An error occurred while fetching data: {e}", status=500)
    return view_function

def x_render_with_api_data__mutmut_7(api_endpoint, template_name):
    """
    Generic function to render a template with data fetched from the API.

    Args:
        api_endpoint (str): The API endpoint to fetch data from.
        template_name (str): The name of the template to render.

    Returns:
        function: A view function that renders the specified template.
    """
    @login_required(login_url='login/')
    def view_function(request):
        try:
            url = settings.BASE_API_URL.format(settings.CONTAINER_USERNAME) + api_endpoint
            return fetch_api_data( template_name)
        except Exception as e:
            return HttpResponse(f"An error occurred while fetching data: {e}", status=500)
    return view_function

def x_render_with_api_data__mutmut_8(api_endpoint, template_name):
    """
    Generic function to render a template with data fetched from the API.

    Args:
        api_endpoint (str): The API endpoint to fetch data from.
        template_name (str): The name of the template to render.

    Returns:
        function: A view function that renders the specified template.
    """
    @login_required(login_url='login/')
    def view_function(request):
        try:
            url = settings.BASE_API_URL.format(settings.CONTAINER_USERNAME) + api_endpoint
            return fetch_api_data(url,)
        except Exception as e:
            return HttpResponse(f"An error occurred while fetching data: {e}", status=500)
    return view_function

def x_render_with_api_data__mutmut_9(api_endpoint, template_name):
    """
    Generic function to render a template with data fetched from the API.

    Args:
        api_endpoint (str): The API endpoint to fetch data from.
        template_name (str): The name of the template to render.

    Returns:
        function: A view function that renders the specified template.
    """
    @login_required(login_url='login/')
    def view_function(request):
        try:
            url = settings.BASE_API_URL.format(settings.CONTAINER_USERNAME) + api_endpoint
            return fetch_api_data(url, template_name)
        except Exception as e:
            return HttpResponse(f"An error occurred while fetching data: {e}", status=501)
    return view_function

def x_render_with_api_data__mutmut_10(api_endpoint, template_name):
    """
    Generic function to render a template with data fetched from the API.

    Args:
        api_endpoint (str): The API endpoint to fetch data from.
        template_name (str): The name of the template to render.

    Returns:
        function: A view function that renders the specified template.
    """
    @login_required(login_url='login/')
    def view_function(request):
        try:
            url = settings.BASE_API_URL.format(settings.CONTAINER_USERNAME) + api_endpoint
            return fetch_api_data(url, template_name)
        except Exception as e:
            return HttpResponse(f"An error occurred while fetching data: {e}",)
    return view_function

x_render_with_api_data__mutmut_mutants = {
'x_render_with_api_data__mutmut_1': x_render_with_api_data__mutmut_1, 
    'x_render_with_api_data__mutmut_2': x_render_with_api_data__mutmut_2, 
    'x_render_with_api_data__mutmut_3': x_render_with_api_data__mutmut_3, 
    'x_render_with_api_data__mutmut_4': x_render_with_api_data__mutmut_4, 
    'x_render_with_api_data__mutmut_5': x_render_with_api_data__mutmut_5, 
    'x_render_with_api_data__mutmut_6': x_render_with_api_data__mutmut_6, 
    'x_render_with_api_data__mutmut_7': x_render_with_api_data__mutmut_7, 
    'x_render_with_api_data__mutmut_8': x_render_with_api_data__mutmut_8, 
    'x_render_with_api_data__mutmut_9': x_render_with_api_data__mutmut_9, 
    'x_render_with_api_data__mutmut_10': x_render_with_api_data__mutmut_10
}

def render_with_api_data(*args, **kwargs):
    result = _mutmut_trampoline(x_render_with_api_data__mutmut_orig, x_render_with_api_data__mutmut_mutants, *args, **kwargs)
    return result 

render_with_api_data.__signature__ = _mutmut_signature(x_render_with_api_data__mutmut_orig)
x_render_with_api_data__mutmut_orig.__name__ = 'x_render_with_api_data'



# Views to fetch data from the API and render templates using the generic function
call_motherboards_view = render_with_api_data("api/get_mobos/", 'motherboard_list.html')
call_cpus_view = render_with_api_data("api/get_cpus/", 'cpus_list.html')
call_builds_view = render_with_api_data("api/get_builds/", 'build_list.html')
call_user_builds_view = render_with_api_data("api/get_builds/user/{current_user_id}/", 'build_list.html')
call_rams_view = render_with_api_data("api/get_rams/", 'ram_list.html')
call_storages_view = render_with_api_data("api/get_storages/", 'storage_list.html')
