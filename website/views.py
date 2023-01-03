import datetime
from random import shuffle
from django.shortcuts import render
from website.models import *



def home_page(request):
    testimonials = Testimonials.objects.all()
    updates = HomeUpdates.objects.all()
    events =  HomeEvents.objects.all()
    gallery_imgs = Gallery.objects.all()
    upcomingEvents = UpcomingEvents.objects.all().filter(date__lte=datetime.date.today())
    recruiters = Recruiters.objects.all()
    recruiters3 = recruiters.order_by('?')
    recruiters2 = recruiters.order_by('?')
    achivements = Achivements.objects.order_by('?')
    # recruiters2 = shuffle(recruiters2)

    context = {'Testimonials': testimonials, "updates":updates, "Events": events, "gallery": gallery_imgs,"upcomingEvents": upcomingEvents,"recruiters":recruiters,"recruiters2":recruiters2,"recruiters3":recruiters3,"achivements":achivements}
    return render(request, 'home.html', context=context)


def academics_page(request):

    return render(request, 'academics.html')


def admission_page(request):
    return render(request, 'admission.html')


def campuslife_page(request):
    return render(request, 'campuslife.html')



def about_page(request):
    return render(request, 'about.html')

def nirf_page(request):
    return render(request, 'nirf.html', context={})


def gallery_page(request):
    gallery_imgs = Gallery.objects.order_by('?')
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
