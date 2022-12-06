from hashlib import new
from multiprocessing import context
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import *
from website.models import Gallery, HomeUpdates, Faculty

# Create your views here.


def getDepartment(department):
    match department:
        case "BSH":
            return "Basic Science and Humanities"
        case "CSE":
            return "Computer Science and Engineering"
        case "ECE":
            return "Electronics and Communication Engineering"
        case "EEE":
            return "Electrical and Electronics Engineering"
        case "ME":
            return "Mechanical Engineering"
        case "CE":
            return "Civil Engineering"
        

class Context:
    '''This class is used to pass context to the templates'''
    def __init__(self, dep,route):
        self.dep = dep
        self.title = getDepartment(dep)
        self.gallery = Gallery.objects.filter(department=dep)
        self.updates = HomeUpdates.objects.all()
        self.hero_image = DepHero.objects.filter(department=dep).first()
        self.dep_updates = DepUpdates.objects.filter(department=dep)
        self.route = route
        self.faculties = None
        self.HOD = None
        self.vission = None
        self.mission = None
        self.poes = None
        self.pos = None
        self.psos = None
        self.associations = None
        self.professional_bodies = None
        self.syllabus = None
        self.labs = None
        match route:
            case "about":
                self.vission = Vission.objects.filter(department=dep).first()
                self.mission = Mission.objects.filter(department=dep)
                self.poes = POES.objects.filter(department=dep)
                self.pos = POS.objects.filter(department=dep)
                self.psos = PSOS.objects.filter(department=dep)
            case "faculty":
                self.faculties = Faculty.objects.filter(department=dep).exclude(role__role='HOD')
                self.HOD = Faculty.objects.filter(department=dep).filter(role__role='HOD').first()
            case "associations":
                self.associations = Associations.objects.filter(department=dep)
            case "syllabus":
                self.syllabus = SyllabusPDFS.objects.filter(department=dep)
            case "professionalBodies":
                self.professional_bodies = ProfessionalBodies.objects.filter(department=dep)
            case "labs":
                self.labs = Laboratories.objects.filter(department=dep)
    def data(self):
        '''This method returns the context'''
        return {
            'dep': self.dep,  
            'title': self.title,
            'gallery': self.gallery,
            'updates': self.updates,
            'route': self.route,
            'faculties': self.faculties,
            'HOD': self.HOD,
            'hero_image': self.hero_image,
            'dep_updates': self.dep_updates,
            'vission': self.vission,
            'mission': self.mission,
            'poes': self.poes,
            'pos': self.pos,
            'psos': self.psos,
            'associations': self.associations,
            'professional_bodies': self.professional_bodies,
            'syllabus': self.syllabus,
            'labs':self.labs

        }
def home(request):
    return redirect('BSH/about')
def Department(request, route, department):
    context = Context(department,route).data()
    match route:
            case "about":
                return render(request, 'Departments/index.html', context)
            case "faculty":
                return render(request, 'Departments/Faculty.html', context)
            case "associations":
                return render(request, 'Departments/Associations.html', context)
            case "syllabus":
                return render(request, 'Departments/Syllabus.html', context)
            case "professionalBodies":
                return render(request, 'Departments/ProfessionalBodies.html', context)
            case "labs":
                return render(request, 'Departments/Laboratories.html', context)
            case "achievements":
                return render(request, 'Departments/Achievements.html', context)
            case "events":
                return render(request, 'Departments/Events.html', context)
            case "curriculum_and_syllabus":
                return render(request, 'Departments/curriculum_and_syllabus.html', context)
            case "newsletters":
                return render(request, 'Departments/Newsletters.html', context) 
            case "research":
                return render(request, 'Departments/Research.html', context) 
            case other:
                raise Http404("Page Not Found")     
    
        