import requests
from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


def fetch_api_data(url, template_name):
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


def render_with_api_data(api_endpoint, template_name):
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


# Views to fetch data from the API and render templates using the generic function
call_motherboards_view = render_with_api_data("api/get_mobos/", 'motherboard_list.html')
call_cpus_view = render_with_api_data("api/get_cpus/", 'cpus_list.html')
call_builds_view = render_with_api_data("api/get_builds/", 'build_list.html')
call_user_builds_view = render_with_api_data("api/get_builds/user/{current_user_id}/", 'build_list.html')
call_rams_view = render_with_api_data("api/get_rams/", 'ram_list.html')
call_storages_view = render_with_api_data("api/get_storages/", 'storage_list.html')
