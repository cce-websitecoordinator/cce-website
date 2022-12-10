from django.shortcuts import render
from website.models import *



def home_page(request):
    testimonials = Testimonials.objects.all()
    updates = HomeUpdates.objects.all()
    events =  HomeEvents.objects.all()
    gallery_imgs = Gallery.objects.all()
    upcomingEvents = UpcomingEvents.objects.all()
    recruiters = Recruiters.objects.all()
    context = {'Testimonials': testimonials, "updates":updates, "Events": events, "gallery": gallery_imgs,"upcomingEvents": upcomingEvents,"recruiters":recruiters}
    return render(request, 'home.html', context=context)


def academics_page(request):

    return render(request, 'academics.html')


def admission_page(request):
    return render(request, 'admission.html')


def campuslife_page(request):
    return render(request, 'campuslife.html')


def arts_page(request):
    gallery_imgs = Gallery.objects.all()
    context = {"gallery":gallery_imgs}
    return render(request, 'arts.html', context=context)

def about_page(request):
    return render(request, 'about.html')

def nirf_page(request):
    return render(request, 'nirf.html', context={})


def gallery_page(request):
    gallery_imgs = Gallery.objects.all()
    context = {"gallery":gallery_imgs}
    return render(request, 'gallery.html', context=context)



def alumini_page(request):
    return render(request, 'Alumini.html')

def facilities_page(request):
    context = {
        "facilities": Facilities.objects.all(),
        "hero_img":Hero_Image.objects.all().filter(page="facilities").first(),
        "hero_title":"Facilities"
    }
    return render(request, 'facilities.html' ,context=context)


def test_page(request):
    return render(request, 'Test.html')


def server_error_page(request):
    return render(request, 'Errors/500.html')


def not_found_error_page(request, exception):
    return render(request, 'Errors/404.html')
