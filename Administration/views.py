from django.shortcuts import render

from Administration.models import *
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
    return render(request, 'Administration/PTA.html',context={"PTA_executive_commitee":PTA_executive_commitee,"PTA_members":PTA_members,'hero_image':hero_img,'hero_title':'Parent Teacher Association (PTA)'})

def office_page(request, slug):
    gallery = Gallery.objects.all()[:10];
    staff  = Faculty.objects.filter(department=slug)
    hero_img = Hero_Image.objects.filter(page="office").first()
    title = slug.replace("_"," ") + " (Office)"
    print(title)
    context = {'hero_img':hero_img,"office_data":staff,"slug":slug,'hero_title':title,"gallery":gallery}
    return render(request,'Administration/office_{}.html'.format(slug),context)

           
        
def  anti_ragging_cell_page(request):
    hero_img = Hero_Image.objects.filter(page="antiraging_cell").first()
    anti_ragging_cell_data = AntiRaggingCommittee.objects.all()
    return render(request,'Administration/anti_raging_cell.html',context={'hero_img':hero_img,'hero_title':'Anti Ragging Committee','anti_ragging_cell_data':anti_ragging_cell_data})


def sc_st_monitoring_cell_page(request):
    hero_img = Hero_Image.objects.filter(page="sc_st_monitoring_cell").first()
    sc_st_cell_data = SCSTMonitoringCommittee.objects.all()
    return render(request,'Administration/sc_monitoring_commitee.html',context={'hero_img':hero_img,'hero_title':'SC/ST Monitoring Committee','sc_st_cell_data':sc_st_cell_data})

def examination_cell_page(request):
    hero_img = Hero_Image.objects.filter(page="examination_cell").first()
    faculties = ExaminationCellFaculty.objects.all().first()
    gallery = Gallery.objects.all();
    return render(request,'Administration/examination_cell.html',context={'hero_img':hero_img,'hero_title':'Examination Cell',"faculties":faculties,"gallery":gallery})




def organogram_page(request):
    hero_img = Hero_Image.objects.filter(page="organogram").first()
    gallery = Gallery.objects.all()
    return render(request,'Administration/organogram.html',context={'hero_img':hero_img,'hero_title':'Organogram','gallery':gallery})


def mandatory_disclosure_page(request):
    data = MandatoryDisclosure.objects.all()
    hero_img = Hero_Image.objects.filter(page="mandatory_disclosure").first()
    return render(request,'Administration/mandatory_disclosure.html',context={'hero_img':hero_img,'hero_title':'Mandatory Disclosure','data':data})


def academic_administration_page(request):
    hero_img =Hero_Image.objects.filter(page="academic_research").first()
    data = AcademicAdministration.objects.all().first()
    gallery  = Gallery.objects.all()
    return render(request,"Administration/academic_administration.html",context={'hero_title':'Academic Administartion','hero_img':hero_img,'data':data,'gallery':gallery})