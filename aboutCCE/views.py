from django.shortcuts import render
from aboutCCE.models import *
from website.models import Faculty, Gallery, Hero_Image

# Create your views here.
def management_page(request):
    management_data = Management.objects.all().order_by('order')
    hero_img = Hero_Image.objects.filter(page="management").first()
    context = {
        "management_data": management_data,
         'hero_img':hero_img,
         "hero_title":'Management',
         'gallery':Gallery.objects.all(),
         }
    return render(request, 'aboutCCE/management.html',context=context)

def directors_desk_page(request):
    executive_director = Faculty.objects.filter(role__role="Executive Director").first()
    joint_director_administration = Faculty.objects.filter(role__role="Joint Director Admin").first()
    joint_director_finance = Faculty.objects.filter(role__role="Joint Director Finan").first()
    hero_img = Hero_Image.objects.filter(page="directors_desk").first()
    context = {
        "executive_director": executive_director,
        "joint_director_administration": joint_director_administration,
        "joint_director_finance": joint_director_finance,
        'hero_img':hero_img,
         "hero_title":'Director\'s Desk',
    }
    return render(request, 'aboutCCE/directors_desk.html',context) 

def principals_desk_page(request):
    hero_img = Hero_Image.objects.filter(page="principals_desk").first()
    principal = Faculty.objects.filter(role__role="Principal").first()
    vice_principal = Faculty.objects.filter(role__role="Vice Principal").first()
    context={
        'hero_title':'Principal\'s Desk',
        'hero_img':hero_img,
        'principal':principal,
        "vice_principal":vice_principal,
    }
    return render(request, 'aboutCCE/principals_desk.html',context=context)

def cce_in_media_page(request):
    hero_img = Hero_Image.objects.filter(page="cce_in_media").first()
    cce_in_media_main =  CCEinMedia.objects.all().first()
    cce_in_media_data = CCEinMedia.objects.all()[1:4]
    more_about_cce_data= MoreAboutCCE.objects.all().order_by('-date')
    context = {"cce_in_media_data": cce_in_media_data,'hero_img':hero_img,"hero_title":'CCE in Media',}
    return render(request, 'aboutCCE/cce_in_media.html',context=context)

def committees_page(request):
    hero_img = Hero_Image.objects.filter(page="all_committees").first()
    context = {
         'hero_img':hero_img,
         "hero_title":'Committees',
         'gallery':Gallery.objects.all(),
         }
    return render(request, 'aboutCCE/committees.html',context=context)

def programs_page(request):
    hero_img = Hero_Image.objects.filter(page="programs_offered").first()
    context = {
         'hero_img':hero_img,
         "hero_title":'Programs Offered',
         'gallery':Gallery.objects.all(),
         }
    return render(request, 'aboutCCE/programs.html',context=context)

def hr_manual_page(request):
    hero_img = Hero_Image.objects.filter(page="hr_manual").first()
    context = {
         'hero_img':hero_img,
         "hero_title":'HR Manual',
         'gallery':Gallery.objects.all(),
         }
    return render(request, 'aboutCCE/hr_manual.html',context=context)

def vision_2035_page(request):
    hero_img = Hero_Image.objects.filter(page="vision_2035").first()
    context = {
         'hero_img':hero_img,
         "hero_title":'Vision 2035',
         'gallery':Gallery.objects.all(),
         }
    return render(request, 'aboutCCE/vision_2035.html',context=context)


def annual_report_page(request):
    data = AnnualReport.objects.all()
    hero_img = Hero_Image.objects.filter(page="annual_report").first()
    return render(request,'aboutCCE/annual_report.html',context={'hero_img':hero_img,'hero_title':'Annual Report','data':data}) 


def college_calendar_page(request):
    data = CollegeCalendar.objects.all()
    hero_img = Hero_Image.objects.filter(page="college_calendar").first()
    return render(request,'aboutCCE/college_calendar.html',context={'hero_img':hero_img,'hero_title':'College Calendar','data':data}) 


def college_handbook_page(request):
    hero_img = Hero_Image.objects.filter(page="college_handbook").first()
    context = {
         'hero_img':hero_img,
         "hero_title":'College Handbook',
         'gallery':Gallery.objects.all(),
         }
    return render(request, 'aboutCCE/college_handbook.html',context=context)

def mandatory_disclosure_page(request):
    data = MandatoryDisclosure.objects.all()
    hero_img = Hero_Image.objects.filter(page="mandatory_disclosure").first()
    return render(request,'aboutCCE/mandatory_disclosure.html',context={'hero_img':hero_img,'hero_title':'Mandatory Disclosure','data':data,'route':'mandatory_disclosure'}) 

def ktu_regulations_page(request):
    data = KtuRegulations.objects.all()
    hero_img = Hero_Image.objects.filter(page="ktu_aicte_regulations").first()
    return render(request,'aboutCCE/ktu_regulations.html',context={'hero_img':hero_img,'hero_title':'KTU Regulations','data':data,'route':'ktu_regulations'})

def aicte_approvals_page(request):
    data = AicteApprovals.objects.all()
    hero_img = Hero_Image.objects.filter(page="approvals").first()
    return render(request,'aboutCCE/aicte_approvals.html',context={'hero_img':hero_img,'hero_title':'AICTE Approvals','data':data,'route':'aicte_approvals'})



def audited_statements_page(request):
    data = AuditedStatements.objects.all()
    hero_img = Hero_Image.objects.filter(page="audited_statements").first()
    return render(request,'aboutCCE/audited_statements.html',context={'hero_img':hero_img,'hero_title':'Audited Statements','data':data,'route':'audited_statements'}) 


def college_magazine_page(request):
    data = CollegeMagazine.objects.all()
    hero_img = Hero_Image.objects.filter(page="college_magazine").first()
    return render(request,'aboutCCE/college_magazine.html',context={'hero_img':hero_img,'hero_title':'College Magazine','data':data}) 
