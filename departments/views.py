from hashlib import new
from multiprocessing import context
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import DepHero
from website.models import Gallery, HomeUpdates, Faculty

# Create your views here.




class Context:
    def __init__(self, title,dep,route):
        self.title = title
        self.gallery = Gallery.objects.filter(department=dep)
        self.updates = HomeUpdates.objects.all()
        self.route = route
        self.faculties = Faculty.objects.filter(department=dep).exclude(role__role='HOD')
        self.HOD = Faculty.objects.filter(department=dep).filter(role__role='HOD'),
        self.hero_image = DepHero.objects.filter(department=dep).first()
    
    def data(self):
        return {
            'title': self.title,
            'gallery': self.gallery,
            'updates': self.updates,
            'route': self.route,
            'faculties': self.faculties,
            'HOD': self.HOD,
            'hero_image': self.hero_image
        }
    



def home(request):
    return redirect('BSH/about')


def Department(request, route, department):
    context = Context(department,department,route).data()
    print(context)
    match department:
        case "BSH":
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
        case "ECE":
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
        case "EEE":
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
        case "ME":
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
        case "CE":
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
        case _:
            raise Http404
