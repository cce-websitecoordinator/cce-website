from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from numpy import mat

from website.models import Gallery, HomeUpdates, Faculty

# Create your views here.


def home(request):
    return redirect('BSH-about')


def Department(request, route, department):
    match department:
        case "BSH":
            context = {
                "title": "Basic Sciences and Humanities",
                "gallery": Gallery.objects.all(),
                'updates': HomeUpdates.objects.all(),
                'route': route,
                "faculties": Faculty.objects.filter(department='CSE').exclude(role__role='HOD'),
                "HOD": Faculty.objects.filter(department='CSE').filter(role__role='HOD'),
            }
            match route:
                case "about":
                    return render(request, 'Departments/index.html', context)
                case "faculty":
                    return render(request, 'Departments/Faculty.html', context)
                case "syllabus":
                    return render(request, 'Departments/Syllabus.html', context)
                case "professionalBodies":
                    return render(request, 'Departments/ProfessionalBodies.html', context)
                case "lab":
                    return render(request, 'Departments/Laboratories.html', context)
                case "achievements":
                    return render(request, 'Departments/Achievements.html', context)
                case "events":
                    return render(request, 'Departments/Events.html', context)
                case "newsletters":
                    return render(request, 'Departments/Newsletters.html', context)

        case "CSE":
            return render(request, 'Departments/index.html', context)
        case "ECE":
            return render(request, 'Departments/index.html', context)
        case "EEE":
            return render(request, 'Departments/index.html', context)
        case "ME":
            return render(request, 'Departments/index.html', context)
        case "CE":
            return render(request, 'Departments/index.html', context)

    return HttpResponse(f'Hello {department} {route}')
