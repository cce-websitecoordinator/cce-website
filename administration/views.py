import os
from django.shortcuts import render
from django.http import HttpResponse

from administration.models import *
from website.models import Faculty, Gallery, Hero_Image

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
    gallery = Gallery.objects.all()[:10];
    staff  = Faculty.objects.filter(department=slug)
    hero_img = Hero_Image.objects.filter(page="office").first()
    title = slug.replace("_"," ")
    print(title)
    context = {'hero_img':hero_img,"office_data":staff,"slug":slug,'hero_title':title,"gallery":gallery}
    return render(request,'Administration/office_{}.html'.format(slug),context)

           
        
def  anti_ragging_cell_page(request):
    hero_img = Hero_Image.objects.filter(page="antiraging_cell").first()
    anti_ragging_cell_data = AntiRaggingCommittee.objects.all()
    gallery = Gallery.objects.all();
    return render(request,'Administration/anti_raging_cell.html',context={'hero_img':hero_img,'hero_title':'Anti Ragging Cell','anti_ragging_cell_data':anti_ragging_cell_data,"gallery":gallery})


def sc_st_monitoring_cell_page(request):
    hero_img = Hero_Image.objects.filter(page="sc_st_monitoring_commite").first()
    sc_st_cell_data = SCSTMonitoringCommittee.objects.all()
    gallery = Gallery.objects.all();
    return render(request,'Administration/sc_monitoring_commitee.html',context={'hero_img':hero_img,'hero_title':'SC/ST Monitoring Committee','sc_st_cell_data':sc_st_cell_data,"gallery":gallery})

def examination_cell_page(request):
    hero_img = Hero_Image.objects.filter(page="examination_cell").first()
    faculties = ExaminationCellFaculty.objects.all()
    gallery = Gallery.objects.all();
    return render(request,'Administration/examination_cell.html',context={'hero_img':hero_img,'hero_title':'Examination Cell',"faculties":faculties,"gallery":gallery})




def organogram_page(request):
    hero_img = Hero_Image.objects.filter(page="organogram").first()
    gallery = Gallery.objects.all()
    return render(request,'Administration/organogram.html',context={'hero_img':hero_img,'hero_title':'Organogram','gallery':gallery})



def academic_administration_page(request):
    hero_img =Hero_Image.objects.filter(page="academic_research").first()
    director = AcademicAdministrationDirector.objects.all().first()
    data = AcademicAdministractors.objects.all().order_by('order')
    
    gallery  = Gallery.objects.all().order_by('?')[:10]
    return render(request,"Administration/academic_administration.html",context={'hero_title':'Academic Administration','hero_img':hero_img,'data':data,'director':director,'gallery':gallery})




def grivence_redressal_page(request,slug,page):
    match slug:
        case "index":
            hero_img = Hero_Image.objects.filter(page="grivence_redressal").first()
            data = GrivenceCommitee.objects.all()
            return render(request,"Administration/grievance/index.html",context={'hero_title':'Grievance Redressal','hero_img':hero_img,"slug":slug,"data":data})
        case "staff":
            if page =='login':
                if request.method == "POST":
                    return HttpResponse(request.POST.get('email'))
                else:
                    return render(request,"Administration/grievance/login.html",context={"slug":slug,"page":page})
            else :
                if request.method == "POST":
                    return HttpResponse("gjhdfjgh")
                else:
                    return render(request,"Administration/grievance/signup.html",context={"slug":slug,"page":page})
        case "student":
            return render(request,"Administration/grievance/login.html",context={"slug":slug,"page":page})

        case "women":
            return render(request,"Administration/grievance/login.html",context={"slug":slug,"page":page})

        case "exams":
            return render(request,"Administration/grievance/login.html",context={"slug":slug,"page":page})