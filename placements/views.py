from django.shortcuts import render
from placements.models import PVissionANDMission

from website.models import Hero_Image

# Create your views here.

def placement_page(request,slug):
    context_temp = {
        'title': 'Placements',
        'hero_title': 'Placements',
        'hero_img': Hero_Image.objects.filter(page='placements').first(),
        'dep': slug,
    }
   
    vission = PVissionANDMission.objects.filter(name='Vision').first()
    mission = PVissionANDMission.objects.filter(name='Mission').first()
    objectives = PVissionANDMission.objects.filter(name='objectives')
    context = {**context_temp,vission:vission,mission:mission,objectives:objectives}
    return render(request, 'Placements/index.html',context={**context_temp,'vission':vission,'mission':mission,'objectives':objectives})