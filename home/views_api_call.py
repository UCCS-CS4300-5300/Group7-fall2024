from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import RAM, CPU, Motherboard, Storage
from django.db.models import Q
from rest_framework import viewsets
from .models import Build
from .serializers import BuildSerializer, MotherBoardSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from django.views import generic

import requests
from django.http import HttpResponse

# decorators for verifying that use is logged in
class BuildListView(LoginRequiredMixin, generic.ListView):
    model = Build

#######################
# api call views 
#######################

# Changes recommended by Daniel:
# Apply DRY principle by using helper function

def fetch_api_data(url, template_name):
    result = requests.get(url)
    if result.status_code == 200:
        context = {'data': result.json()}
        return render(None, template_name, context)
    return HttpResponse('Something went wrong', status=500)

# View to show information about all motherboards 
def call_motherboards_view(request):
    url = "https://app-jflinn2-5.devedu.io/api/get_mobos/"
    return fetch_api_data(url, 'motherboard_list.html')



# these views call the api endpoints by creating a url. and then use that url to call the api endpoint
# these views then capture that data and send it to a html template for rendering
# the logic that determines which data from our database
# is sent to html files can be found in views.py

# the order of processing is as follows:

# 1st: create api reference url
# 2nd: call api reference url
# 3rd: api reference url calls a view in views.py
# 4th: the called view in views.py will return serialized information
# 5th: the returned serialized information is sent to a html template for rendering

# show information about all motherboards in our database
# see views.py function "get_mobos" for more information
def call_motherboards_view(request):
    url = "https://app-jflinn2-5.devedu.io/api/get_mobos/"
    result = requests.get(url)
    if result.status_code == 200:
        context = {'data': result.json()}
        return render(request, 'motherboard_list.html', context)
    return HttpResponse('Something went wrong')

# show information about all cpus in our database
# see views.py function "get_cpus" for more information about data returned
def call_cpus_view(request):
    url = "https://app-jflinn2-5.devedu.io/api/get_cpus/"
    result = requests.get(url)
    if result.status_code == 200:
        context = {'data': result.json()}
        return render(request, 'cpus_list.html', context)
    return HttpResponse('Something went wrong')

# show information about all builds in our database
# see views.py function "get_builds" for more information about data returned
def call_builds_view(request):
    url = "https://app-jflinn2-5.devedu.io/api/get_builds/"
    result = requests.get(url)
    if result.status_code == 200:
        context = {'data': result.json()}
        return render(request, 'build_list.html', context)
    return HttpResponse('Something went wrong')

# show information about all builds in our database belonging to the logged in user
# see views.py function get_builds_user for more information related to the result of the api call
@login_required(login_url='login/') # if user is not logged in, redirect to login page
def call_user_builds_view(request):
    current_user = request.user
    current_user_id = current_user.id
    url = "https://app-jflinn2-5.devedu.io/api/get_builds/user" + str(current_user_id) + "/"
    result = requests.get(url)
    if result.status_code == 200:
        context = {'data': result.json()}
        return render(request, 'build_list.html', context)
    return HttpResponse('Something went wrong')

# show information about all rams in our database
# see views.py function "get_rams" for more information about data returned
def call_rams_view(request):
    url = "https://app-jflinn2-5.devedu.io/api/get_rams/"
    result = requests.get(url)
    if result.status_code == 200:
        context = {'data': result.json()}
        return render(request, 'ram_list.html', context)
    return HttpResponse('Something went wrong')

# show information about all storages in our database
# see views.py function "get_storages" for more information about data returned
def call_storages_view(request):
    url = "https://app-jflinn2-5.devedu.io/api/get_storages/"
    result = requests.get(url)
    if result.status_code == 200:
        context = {'data': result.json()}
        return render(request, 'storage_list.html', context)
    return HttpResponse('Something went wrong')