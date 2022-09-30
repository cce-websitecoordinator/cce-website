from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return redirect('BSH')


def BSH(request):
    return render(request, "Departments/index.html")



