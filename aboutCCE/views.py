from django.shortcuts import render

from aboutCCE.models import *

# Create your views here.
def management_page(request):
    management_data = Management.objects.all()
    context = {"management_data": management_data}
    return render(request, 'aboutCCE/management.html',context=context)

def directors_desk_page(request):
    return render(request, 'aboutCCE/directors_desk.html') 

def principals_desk_page(request):
    return render(request, 'aboutCCE/principals_desk.html')

def cce_in_media_page(request):
    # print(CCEinMedia.objects.all().first())
    # "more_about_cce_data": MoreAboutCCE.objects.all(),
    # "cce_in_media_data": CCEinMedia.objects.all()[1:4]
    context = {"cce_in_media_main": CCEinMedia.objects.all().first(),"cce_in_media_data": CCEinMedia.objects.all()[1:4],"more_about_cce_data": MoreAboutCCE.objects.all()}
    return render(request, 'aboutCCE/cce_in_media.html',context=context)