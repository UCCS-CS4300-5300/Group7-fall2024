from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import RAM, CPU, Motherboard, Storage
from django.db.models import Q
from rest_framework import viewsets
from .models import Build
from .serializers import BuildSerializer, MotherBoardSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
from django.http import HttpResponse


def call_motherboard_view(request):
    url = "https://app-jflinn2-5.devedu.io/api/get_mobos/"
    
    result = requests.get(url)
    if result.status_code == 200:
        print(result.json())
        return HttpResponse(result.json())
    return HttpResponse('Something went wrong')