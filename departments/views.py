from multiprocessing import context
from django.shortcuts import redirect, render

from website.models import Gallery,HomeUpdates

# Create your views here.
def home(request):
    return redirect('BSH/home')



def Department(request,route,department):
    
    if route  == "home":
        context={
        "title":"Basic Sciences and Humanities",
        "gallery":Gallery.objects.all(),
        'updates':HomeUpdates.objects.all()
        }
        return render(request,"Departments/index.html",context=context)
    
   
    return render(request, "Departments/index.html",context=context)

