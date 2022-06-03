from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def academics_page(request):
    return render(request, 'academics.html')


def departments_page(request):
    return render(request, 'departments.html')


def campuslife_page(request):
    return render(request, 'campuslife.html')


def about_page(request):
    return render(request, 'about.html')
