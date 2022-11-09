from django.shortcuts import render
from website.models import *


def home_page(request):
    context = {'Testimonials': Testimonials.objects.all(), "name": "John Doe","updates":HomeUpdates.objects.all(),"Events":HomeEvents.objects.all(),"gallery":Gallery.objects.all()}
    return render(request, 'home.html', context=context)


def academics_page(request):

    return render(request, 'academics.html')

def admission_page(request):
    return render(request, 'admission.html')

def campuslife_page(request):
    return render(request, 'campuslife.html')

def arts_page(request):
    return render(request, 'arts.html')

def governing_body__page(request):
    return render(request, 'Governing_body.html')

def about_page(request):
    return render(request, 'about.html')

def nirf_page(request):
    return render(request, 'nirf.html',context={})

def gallery_page(request):
    return render(request, 'gallery.html')

def iqac_page(request):
    return render(request, 'iqac.html')


def test_page(request):
    return render(request, 'Test.html')


def server_error_page(request):
    return render(request, 'Errors/500.html')

def not_found_error_page(request,exception):
    return render(request, 'Errors/404.html')
