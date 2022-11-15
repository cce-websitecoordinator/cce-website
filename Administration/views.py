from django.shortcuts import render

from Administration.models import GoverningBody

# Create your views here.
def governing_body(request):
    governing_body_data = GoverningBody.objects.all()
    context = {
        "governing_body_data": governing_body_data,
    }
    return render(request, "Administration/governing_body.html", context)