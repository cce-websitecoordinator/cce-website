from django.shortcuts import render

from Administration.models import *
from website.models import Faculty, Hero_Image

# Create your views here.
def governing_body(request):
    governing_body_data = GoverningBodyMembers.objects.all()
    hero_img = Hero_Image.objects.filter(page="governing_body").first()
    context = {
        "governing_body_data": governing_body_data,
        "hero_img": hero_img,
        'hero_title':'Governing Body',
        "governing_body_order_file": GoverningBodyOrderFile.objects.all().first(),

    }
    return render(request, "Administration/governing_body.html", context)

def iqac_page(request):
    IQAC_executive_commitee = IQACExecutiveCommitee.objects.all()
    formation_notice = IQACFormationNotice.objects.all()
    hero_img = Hero_Image.objects.filter(page="iqac").first()
    return render(request, 'Administration/IQAC.html',context={"IQAC_executive_commitee":IQAC_executive_commitee,"formation_notice":formation_notice,'hero_img':hero_img,'hero_title':'Internal Quality Assurance Cell (IQAC)'})


def pta_page(request):
    PTA_executive_commitee = PTAExecutiveCommitee.objects.all()
    PTA_members = PTAMembers.objects.all()
    hero_img = Hero_Image.objects.filter(page="pta").first()
    return render(request, 'Administration/PTA.html',context={"PTA_executive_commitee":PTA_executive_commitee,"PTA_members":PTA_members,'hero_img':hero_img,'hero_title':'Parent Teacher Association (PTA)'})

def office_page(request, slug):
    staff  = Faculty.objects.filter(department=slug).order_by('priorities')
    hero_img = Hero_Image.objects.filter(page="office").first()
    context = {'hero_img':hero_img,"staff":staff}
    return render(request,'Administration/office_{}'.format(slug),context)

           
        
