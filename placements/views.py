from django.shortcuts import render

from website.models import Hero_Image

# Create your views here.

def placement_page(request,slug):
    context_temp = {
        'title': 'Placements',
        'hero_title': 'Placements',
        'hero_img': Hero_Image.objects.filter(page='placements').first(),
        'dep': slug,
    }
    context = {**context_temp}
    return render(request, 'Placements/index.html',context=context)