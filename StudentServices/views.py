from django.shortcuts import render
from StudentServices.models import *
from website.models import Gallery, Hero_Image

# Create your views here.
def arts_page(request):
    arts_updates = Artsupdates.objects.all()
    gallery_imgs = ArtsGallery.objects.all()
    hero_img = Hero_Image.objects.all().filter(page="arts").first
    context = {'arts_updates':arts_updates,"events":ArtsEvents.objects.all(),"teams":artsTeamStatus.objects.all(),"gallery":gallery_imgs,"hero_img":hero_img,"hero_title":"Arts"}
    return render(request, 'StudentServices/arts.html',context=context)



def sports_page(request):
    arts_updates = SportsUpdates.objects.all()
    gallery_imgs = SportsGallery.objects.all()
    events = SportsEvents.objects.all()
    teams = SportsTeamStatus.objects.all()
    hero_img = Hero_Image.objects.all().filter(page="sports").first
    context = {'arts_updates':arts_updates,"events":events,"teams":teams,"gallery":gallery_imgs,"hero_img":hero_img,"hero_title":"Sports"}
    return render(request, 'StudentServices/sports.html',context=context)

def nss_page(request):
    return render(request, 'StudentServices/nss.html',context={})

def iic_page(request):
    hero_img = Hero_Image.objects.all().filter(page="iic").first
    members = IICCommitee.objects.all()
    certificates = IICCertificate.objects.all()
    return render(request, 'StudentServices/iic.html',context={"hero_img":hero_img,"hero_title":"Institution’s Innovation Council","members":members,"certificates":certificates})


def clubs_page(request):
    data = Clubs.objects.all()
    hero_img = Hero_Image.objects.all().filter(page="clubs").first

    return render(request, 'StudentServices/clubs.html',context={"data":data,"hero_img":hero_img,"hero_title":"Clubs"})