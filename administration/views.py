import os,csv
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from utils.test_mail import send_email

from administration.models import *
from cce import settings
from website.models import Faculty, Gallery, Hero_Image
from .forms import GrievanceBodyForm

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
    minutes = IQACMeetingMinutes.objects.all()
    year = [nested_tuple[0] for nested_tuple in ACADEMIC_YEARS[::-1]]
    return render(request, 'Administration/IQAC.html',context={"IQAC_executive_commitee":IQAC_executive_commitee,"formation_notice":formation_notice,'hero_img':hero_img,'hero_title':'Internal Quality Assurance Cell (IQAC)',"minutes":minutes,"years":year})


def pta_page(request):
    hero_img = Hero_Image.objects.filter(page="pta").first()
    years = [year[0] for year in PTAExecutiveCommitee.objects.values_list('year').distinct()]
    context_temp = {'hero_img':hero_img,'hero_title':'Parent Teacher Association (PTA)',"years":years}
    if request.method == "GET":
        if yr := request.GET.get("year"):
            PTA_executive_commitee = PTAExecutiveCommitee.objects.all().filter(year = yr)
            PTA_members = PTAMembers.objects.all().filter(year = yr)
            context = {**context_temp,"PTA_executive_commitee":PTA_executive_commitee,"PTA_members":PTA_members,"year":yr}
        else:
            PTA_executive_commitee = PTAExecutiveCommitee.objects.all().filter(year = years[0])
            PTA_members = PTAMembers.objects.all().filter(year = years[0])
            context = {**context_temp,"PTA_executive_commitee":PTA_executive_commitee,"PTA_members":PTA_members,"year":years[0]}            

        return render(request, 'Administration/PTA.html',context=context)
    else:
        return Http404("Page Not Found")
    

def office_page(request, slug):
    gallery = Gallery.objects.all().order_by('?')[:10];
    staff  = Faculty.objects.filter(department=slug)
    hero_img = Hero_Image.objects.filter(page="office").first()
    title = slug.replace("_"," ")
    print(title)
    context = {'hero_img':hero_img,"office_data":staff,"slug":slug,'hero_title':title,"gallery":gallery}
    return render(request, f'Administration/office_{slug}.html', context)

           
        
def  anti_ragging_cell_page(request):
    hero_img = Hero_Image.objects.filter(page="antiraging_cell").first()
    anti_ragging_cell_data = AntiRaggingCommittee.objects.all()
    gallery = Gallery.objects.all().order_by('?')[:6];
    return render(request,'Administration/anti_raging_cell.html',context={'hero_img':hero_img,'hero_title':'Anti Ragging Cell','anti_ragging_cell_data':anti_ragging_cell_data,"gallery":gallery})


def sc_st_monitoring_cell_page(request):
    hero_img = Hero_Image.objects.filter(page="sc_st_monitoring_commite").first()
    sc_st_cell_data = SCSTMonitoringCommittee.objects.all()
    gallery = Gallery.objects.all().order_by('?')[:6];
    return render(request,'Administration/sc_monitoring_commitee.html',context={'hero_img':hero_img,'hero_title':'SC/ST Monitoring Committee','sc_st_cell_data':sc_st_cell_data,"gallery":gallery})

def examination_cell_page(request):
    hero_img = Hero_Image.objects.filter(page="examination_cell").first()
    faculties = ExaminationCellFaculty.objects.all()
    gallery = Gallery.objects.all().order_by('?')[:6];
    return render(request,'Administration/examination_cell.html',context={'hero_img':hero_img,'hero_title':'Examination Cell',"faculties":faculties,"gallery":gallery})




def organogram_page(request):
    hero_img = Hero_Image.objects.filter(page="organogram").first()
    gallery = Gallery.objects.all().order_by('?')[:6]
    return render(request,'Administration/organogram.html',context={'hero_img':hero_img,'hero_title':'Organogram','gallery':gallery})



def academic_administration_page(request):
    hero_img =Hero_Image.objects.filter(page="academic_research").first()
    principal = AcademicAdministrationDirector.objects.filter(director_reserch_role="principal").first()
    vice_principal = AcademicAdministrationDirector.objects.filter(director_reserch_role="vice_principal").first()
    aca_dir = AcademicAdministrationDirector.objects.filter(director_reserch_role="aca_dir").first()
    res_dir = AcademicAdministrationDirector.objects.filter(director_reserch_role="res_dir").first()
    data = AcademicAdministractors.objects.all().order_by('order')
    gallery  = Gallery.objects.all().order_by('?')[:10]
    return render(request,"Administration/academic_administration.html",context={'hero_title':'Academic Administration','hero_img':hero_img,'data':data,'principal':principal,'vice_principal':vice_principal,'aca_dir':aca_dir,'res_dir':res_dir,'gallery':gallery})




def grivence_redressal_index_page(request):
    hero_img = Hero_Image.objects.filter(page="grivence_redressal").first()
    data = GrivenceCommitee.objects.all()
    return render(request,"Administration/grievance/index.html",context={'hero_title':'Grievance Redressal','hero_img':hero_img,"data":data})




def grivence_redressal_page(request, slug=None, page=None):
    # sourcery skip: extract-method
    print(slug)
    if slug is None and page is None:
        raise Http404("Page Not Found")

    if page == 'login':
        return handle_login(request, slug, page)  # Use a separate function for login handling

    elif page == 'dashboard':
        user_data = request.session.get('email')
        user_name = request.session.get('name')
        user_type = request.session.get('type')
        if user_data is None:
            return render(request, "Administration/grievance/login.html", context={"slug": slug, "page": "login"})

        if request.method == 'POST':
            form = GrievanceBodyForm(request.POST)  
            if form.is_valid():
                grievance_instance = form.save(commit=False)  
                grievance_instance.email = user_data  
                grievance_instance.save()
                subject = "Grievance Submission - CCE"
                message = "This is a sample email message."
                recipient_email = grievance_instance.email
                template_variables = {"name":grievance_instance.name,'date':datetime.date,'email':recipient_email,"data":"Arum enthum Paranjallum Amal Ettan Uyir Annu First Years NNU"}
                try:
                    response = send_email(subject,message, recipient_email,template_values=template_variables)
                    print(response)
                    return HttpResponse(response)
                except Exception as e:
                    return HttpResponse(e)
                return render(request, "Administration/grievance/form.html", context={"slug": slug, "page": page, "form": form})

        else:
            form = GrievanceBodyForm(initial={"email": user_data,"name":user_name,"type":user_type})

        return render(request, "Administration/grievance/form.html", context={"slug": slug, "page": page, "form": form})

    elif page == 'logout':
        del request.session['email']
        return render(request, "Administration/grievance/login.html", context={"slug": slug, "page": "login"})

def handle_login(request, slug, page):
    print("slug : ",slug)


    if request.method != "POST":
        return render(request, "Administration/grievance/login.html", context={"slug": slug, "page": page})


    email = request.POST["email"]
    password = request.POST["password"]
    user = GrivenceUser.objects.filter(email=email).first()

    print(user.type)

    if user.type != slug:
        return render(
            request,
            "Administration/grievance/login.html",
            context={
                "slug": slug,
                "page": page,
                "error": f"Not {slug} account.",
            },
        )

    if not user:
        return render(request, "Administration/grievance/login.html", context={"slug": slug, "page": page, "error": "Invalid Email"})

    if password != user.password:
        return render(request, "Administration/grievance/login.html", context={"slug": slug, "page": page, "error": "Wrong Password"})

    request.session['email'] = email
    request.session['name'] = user.name
    request.session['type'] = user.type
    redirect_url = f"/administration/grievance/{slug}/dashboard"
    return redirect(redirect_url)

   
def test_fn(request):

    subject = "Sample Email Subject"
    message = "This is a sample email message."
    sender_email = "grievance@cce.edu.in"
    recipient_email = 'magniyadavis@cce.edu.in'
    template_variables = {"name":"Amal Ettan Uyir",'date':datetime.date,'email':recipient_email,"data":"Arum enthum Paranjallum Amal Ettan Uyir Annu First Years NNU"}
    try:
        response = send_email(subject,message, recipient_email,template_values=template_variables)
        print(response)
        return HttpResponse(response)
    except Exception as e:
        return HttpResponse(e)


    return HttpResponse(f"{smtp_port} {smtp_password} {smtp_username}")
