from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello from App')


def signup(request):
    return HttpResponse('Signup page!')
