from django.shortcuts import render

from aboutCCE.models import *
from website.models import Faculty, Hero_Image

# Create your views here.
def management_page(request):
    management_data = Management.objects.all()
    context = {"management_data": management_data}
    return render(request, 'aboutCCE/management.html',context=context)

def directors_desk_page(request):
    return render(request, 'aboutCCE/directors_desk.html') 

def principals_desk_page(request):
    hero_img = Hero_Image.objects.filter(page="principals_desk").first()
    principal = Faculty.objects.filter(role__role="Principal").first()
    vice_principal = Faculty.objects.filter(role__role="Vice Principal").first()
    context={
        'hero_title':'Principal\'s Desk',
        'hero_img':hero_img,
        'principal':principal,
        "vice_principal":vice_principal,
    }
    return render(request, 'aboutCCE/principals_desk.html',context=context)

def cce_in_media_page(request):
    cce_in_media_main =  CCEinMedia.objects.all().first()
    cce_in_media_data = CCEinMedia.objects.all()[1:4]
    more_about_cce_data= MoreAboutCCE.objects.all()
    context = {"cce_in_media_main":cce_in_media_main,"cce_in_media_data": cce_in_media_data,"more_about_cce_data": more_about_cce_data}
    return render(request, 'aboutCCE/cce_in_media.html',context=context)