from multiprocessing import context
from django.shortcuts import redirect, render

from website.models import Gallery,HomeUpdates

# Create your views here.
def home(request):
    return redirect('BSH/home')

def depHome(request):
    return redirect('home')


def BSH(request,route):
    print(route)
    if route  == "home":
        context={
        "title":"Basic Sciences and Humanities",
        "gallery":Gallery.objects.all(),
        'updates':HomeUpdates.objects.all()
        }
        return render(request,"Departments/index.html",context=context)
    if route  == "faculty":
        context={
        "title":"Faculty Basic Sciences and Humanities",
        "gallery":Gallery.objects.all(),
        'updates':HomeUpdates.objects.all()
        }
        return render(request,"Departments/Faculty.html",context=context)
   
    return render(request, "Departments/index.html",context=context)






