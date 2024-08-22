from django.shortcuts import render
from departments.models import Placements
from placements.models import *

from website.models import Gallery, Hero_Image, Recruiters

# Create your views here.

def placement_page(request,slug):
    context_temp = {
        'title': 'Placements',
        'hero_title': 'Placements',
        'hero_img': Hero_Image.objects.filter(page='placements').first(),
        'route': slug,
    }
    context={**context_temp}
    match slug:
        case 'index':
            vission = PVissionANDMission.objects.filter(name='Vision').first()
            mission = PVissionANDMission.objects.filter(name='Mission').first()
            objectives = PVissionANDMission.objects.filter(name='objectives')
            testimonials = Testimonials.objects.all()
            recruiters = Recruiters.objects.all()
            recruiters3 = recruiters.order_by('?')
            recruiters2 = recruiters.order_by('?')
            side_updates = PlacementUpdates.objects.all().order_by('-date')
            gallery = Gallery.objects.all().order_by('?')[:6]
            context = {**context_temp,'vission':vission,'mission':mission,'objectives':objectives,'testimonials':testimonials,"recruiters": recruiters, "recruiters2": recruiters2, "recruiters3": recruiters3,"side_updates":side_updates,"gallery":gallery}
            return render(request, 'Placements/index.html',context=context)
        case "placement_traning":
            context = {**context_temp,'data':PlacementTraning.objects.all(),"list":PlacementList.objects.all().order_by('-year')}
            return render(request, 'Placements/placement_traning.html',context=context)
        case "achivements":
            deps = ['CE','CSE','ECE','EEE','ME']
            if request.method == "GET":
                dep = request.GET.get("dep")
                if dep:
                    placement = Placements.objects.filter(department = dep).all().order_by('-year')
                else:
                    dep = "CE"
                    placement = Placements.objects.filter(department = "CE").all().order_by('-year')
            else:
                placement = None
            context = {**context_temp,"achivements":Achivements.objects.all(),"placement":placement,"dep":dep,"deps":deps}
            return render(request, 'Placements/achivements.html',context=context)
        case "faculty":
            context = {**context_temp,"faculty":PlacementFaculty.objects.all().order_by('order')}
            return render(request, 'Placements/faculty.html',context=context)
        case "statistics":
            image = PlacementStatistics.objects.all()
            table = PlacementStatsTable.objects.all()
            batchtable = Tables.objects.all()
            context = {**context_temp,"image":image,"table":table,"batch":batchtable}
            return render(request, 'Placements/statistics.html',context=context)
        case "activities":
            return render(request, 'Placements/activities.html',context=context)
        case "recruiters":
            return render(request, 'Placements/recruiters.html',context=context)

    