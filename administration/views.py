import os, csv
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from utils.seed_users import seed_database
from utils.test_mail import send_email
from django.contrib.auth.hashers import check_password, make_password
from django.templatetags.static import static

# Ensure MeetingMinutes is imported
from administration.models import *
from administration.models import MeetingMinutes 

from cce import settings
from website.models import Faculty, Gallery, Hero_Image
from .forms import GrievanceBodyForm


# Create your views here.
def governing_body(request):
    governing_body_data = GoverningBodyMembers.objects.all().order_by("order", "id")
    hero_img = Hero_Image.objects.filter(page="governing_body").first()
    context = {
        "governing_body_data": governing_body_data,
        "hero_img": hero_img,
        "hero_title": "Governing Body",
        "governing_body_order_file": GoverningBodyOrderFile.objects.all().first(),
    }
    return render(request, "Administration/governing_body.html", context)


def iqac_page(request):
    IQAC_executive_commitee = IQACExecutiveCommitee.objects.all().order_by("priority")
    formation_notice = IQACFormationNotice.objects.all()
    hero_img = Hero_Image.objects.filter(page="iqac").first()
    minutes = IQACMeetingMinutes.objects.all()
    year = [nested_tuple[0] for nested_tuple in ACADEMIC_YEARS[::-1]]
    return render(
        request,
        "Administration/IQAC.html",
        context={
            "IQAC_executive_commitee": IQAC_executive_commitee,
            "formation_notice": formation_notice,
            "hero_img": hero_img,
            "hero_title": "Internal Quality Assurance Cell (IQAC)",
            "minutes": minutes,
            "years": year,
        },
    )


def pta_page(request):
    hero_img = Hero_Image.objects.filter(page="pta").first()
    years = [
        year[0] for year in PTAExecutiveCommitee.objects.values_list("year").distinct()
    ]
    context_temp = {
        "hero_img": hero_img,
        "hero_title": "Parent Teacher Association (PTA)",
        "years": years,
    }
    if request.method == "GET":
        if yr := request.GET.get("year"):
            PTA_executive_commitee = PTAExecutiveCommitee.objects.all().filter(year=yr)
            PTA_members = PTAMembers.objects.all().filter(year=yr)
            context = {
                **context_temp,
                "PTA_executive_commitee": PTA_executive_commitee,
                "PTA_members": PTA_members,
                "year": yr,
            }
        else:
            PTA_executive_commitee = PTAExecutiveCommitee.objects.all().filter(
                year=years[0]
            )
            PTA_members = PTAMembers.objects.all().filter(year=years[0])
            context = {
                **context_temp,
                "PTA_executive_commitee": PTA_executive_commitee,
                "PTA_members": PTA_members,
                "year": years[0],
            }

        return render(request, "Administration/PTA.html", context=context)
    else:
        return Http404("Page Not Found")


def office_page(request, slug):
    gallery = Gallery.objects.all().order_by("?")[:10]
    staff = Faculty.objects.filter(department=slug).order_by("priorities")
    hero_img = Hero_Image.objects.filter(page="office").first()
    title = slug.replace("_", " ")
    print(title)
    context = {
        "hero_img": hero_img,
        "office_data": staff,
        "slug": slug,
        "hero_title": title,
        "gallery": gallery,
    }
    return render(request, f"Administration/office_{slug}.html", context)


def anti_ragging_cell_page(request):
    hero_img = Hero_Image.objects.filter(page="antiraging_cell").first()
    anti_ragging_cell_data = AntiRaggingCommittee.objects.all()
    gallery = Gallery.objects.all().order_by("?")[:6]
    return render(
        request,
        "Administration/anti_raging_cell.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Anti Ragging Cell",
            "anti_ragging_cell_data": anti_ragging_cell_data,
            "gallery": gallery,
        },
    )


def sc_st_monitoring_cell_page(request):
    hero_img = Hero_Image.objects.filter(page="sc_st_monitoring_commite").first()
    sc_st_cell_data = SCSTMonitoringCommittee.objects.all()
    gallery = Gallery.objects.all().order_by("?")[:6]
    
    # === ADDED MINUTES FETCH ===
    minutes = MeetingMinutes.objects.filter(category="sc_st").order_by('-date')
    
    return render(
        request,
        "Administration/sc_monitoring_commitee.html",
        context={
            "hero_img": hero_img,
            "hero_title": "SC/ST Monitoring Committee",
            "sc_st_cell_data": sc_st_cell_data,
            "gallery": gallery,
            "minutes": minutes, # <--- Added to context
        },
    )


def examination_cell_page(request):
    hero_img = Hero_Image.objects.filter(page="examination_cell").first()
    faculties = ExaminationCellFaculty.objects.all()
    rules = ExaminationCellRules.objects.first()
    gallery = Gallery.objects.all().order_by("?")[:6]
    return render(
        request,
        "Administration/examination_cell.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Examination Cell",
            "faculties": faculties,
            "gallery": gallery,
            "rules": rules,
        },
    )


def organogram_page(request):
    hero_img = Hero_Image.objects.filter(page="organogram").first()
    gallery = Gallery.objects.all().order_by("?")[:6]
    return render(
        request,
        "Administration/organogram.html",
        context={"hero_img": hero_img, "hero_title": "Organogram", "gallery": gallery},
    )


def academic_administration_page(request):
    hero_img = Hero_Image.objects.filter(page="academic_research").first()
    principal = AcademicAdministrationDirector.objects.filter(
        director_reserch_role="principal"
    ).first()
    vice_principal = AcademicAdministrationDirector.objects.filter(
        director_reserch_role="vice_principal"
    ).first()
    aca_dir = AcademicAdministrationDirector.objects.filter(
        director_reserch_role="aca_dir"
    ).first()
    res_dir = AcademicAdministrationDirector.objects.filter(
        director_reserch_role="res_dir"
    ).first()
    out_dir = AcademicAdministrationDirector.objects.filter(
        director_reserch_role="out_dir"
    ).first()
    data = AcademicAdministractors.objects.all().order_by("order")
    gallery = Gallery.objects.all().order_by("?")[:10]
    return render(
        request,
        "Administration/academic_administration.html",
        context={
            "hero_title": "Academic Administration",
            "hero_img": hero_img,
            "data": data,
            "principal": principal,
            "vice_principal": vice_principal,
            "aca_dir": aca_dir,
            "res_dir": res_dir,
            "gallery": gallery,
        },
    )


def grivence_redressal_index_page(request):
    hero_img = Hero_Image.objects.filter(page="grivence_redressal_sysytem").first()
    data = GrivenceCommitee.objects.all()
    return render(
        request,
        "Administration/grievance/index.html",
        context={
            "hero_title": "Grievance/Suggestions",
            "hero_img": hero_img,
            "data": data,
        },
    )


def grivence_redressal_page(request, slug=None, page=None):
    if slug is None and page is None:
        raise Http404("Page Not Found")

    if page == "login":
        return handle_login(
            request, slug, page
        )  # Use a separate function for login handling

    elif page == "dashboard":
        user_data = request.session.get("email")
        user_name = request.session.get("name")
        user_type = request.session.get("type")
        if user_data is None:
            return render(
                request,
                "Administration/grievance/login.html",
                context={"slug": slug, "page": "login"},
            )

        if request.method == "POST":
            form = GrievanceBodyForm(request.POST)
            if form.is_valid():
                grievance_instance = form.save(commit=False)
                grievance_instance.email = user_data
                grievance_instance.save()

                name = grievance_instance.name
                subject = grievance_instance.subject
                message = grievance_instance.message
                recipient_email = grievance_instance.email

                template_variables = {
                    "name": name,
                    "date": datetime.date,
                    "email": recipient_email,
                    "data": message,
                }
                try:
                    response,error = send_email(
                        subject,
                        message,
                        recipient_email,
                        template_values=template_variables,
                    )
                    if response:
                        success_message = f"Grievance submitted successfully!"
                        return render(
                            request,
                            "Administration/grievance/form.html",
                            context={
                                "slug": slug,
                                "page": page,
                                "form": form,
                                "res": success_message,
                            },
                        )
                    else:
                        return render(
                            request,
                            "Administration/grievance/form.html",
                            context={
                                "slug": slug,
                                "page": page,
                                "form": form,
                                "error": error,
                            },
                        )
                except Exception as e:
                    return render(
                        request,
                        "Administration/grievance/form.html",
                        context={"slug": slug, "page": page, "form": form, "error": str(e)},
                    )
                # return render(
                #     request,
                #     "Administration/grievance/form.html",
                #     context={"slug": slug, "page": page, "form": form},
                # )

        else:
            form = GrievanceBodyForm(
                initial={"email": user_data, "name": user_name, "type": user_type}
            )

        return render(
            request,
            "Administration/grievance/form.html",
            context={"slug": slug, "page": page, "form": form},
        )

    elif page == "logout":
        del request.session["email"]
        return render(
            request,
            "Administration/grievance/login.html",
            context={"slug": slug, "page": "login"},
        )


def handle_login(request, slug, page):
    if request.method != "POST":
        return render(
            request,
            "Administration/grievance/login.html",
            context={"slug": slug, "page": page},
        )

    email = request.POST["email"]
    password = request.POST["password"]
    user = GrivenceUser.objects.filter(email=email).first()

    if not user:
        return render(
            request,
            "Administration/grievance/login.html",
            context={"slug": slug, "page": page, "error": "Invalid Email"},
        )

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

    if check_password(password, user.password):
        pass  # valid hashed password
    elif user.password == password:
        # legacy plain-text match: re-hash and save
        user.password = make_password(password)
        user.save()
    else:
        return render(
            request,
            "Administration/grievance/login.html",
            context={"slug": slug, "page": page, "error": "Wrong Password"},
        )
    request.session["email"] = email
    request.session["name"] = user.name
    request.session["type"] = user.type
    redirect_url = f"/administration/grievance/{slug}/dashboard"
    return redirect(redirect_url)


def test_fn(request):
    subject = "Sample Email Subject"
    message = "This is a sample email message."
    sender_email = "grievance@cce.edu.in"
    recipient_email = "magniyadavis@cce.edu.in"
    template_variables = {
        "name": "Amal Ettan Uyir",
        "date": datetime.date,
        "email": recipient_email,
        "data": "Arum enthum Paranjallum Amal Ettan Uyir Annu First Years NNU",
    }
    try:
        response = send_email(
            subject, message, recipient_email, template_values=template_variables
        )
        print(response)
        return HttpResponse(response)
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse(f"{smtp_port} {smtp_password} {smtp_username}")


def disciplinary_committee_page(request):
    hero_img = Hero_Image.objects.filter(page="disciplinary_committee").first()
    disciplinary_committee_data = DisciplinaryCommittee.objects.all()
    hero_img = Hero_Image.objects.all().filter(page="disciplinary_committee").first()
    gallery = Gallery.objects.all().order_by("?")[:6]
    return render(
        request,
        "Administration/disciplinary_committee.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Disciplinary Committee",
            "data": disciplinary_committee_data,
            "gallery": gallery,
        },
    )


def internal_audit_page(request):
    hero_img = Hero_Image.objects.all().filter(page="internal_audit_page").first()
    data = InternalAuditAbout.objects.first()
    internal_audit_data = InternalAudit.objects.all()
    return render(
        request,
        "Administration/internal_audit.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Internal Audit",
            "data": data,
            "internal_audit_data": internal_audit_data,
        },
    )


def external_audit_page(request):
    hero_img = Hero_Image.objects.filter(page="external_audit_page").first()
    data = ExternalAudit.objects.first()
    return render(
        request,
        "Administration/external_audit.html",
        context={"hero_img": hero_img, "hero_title": "External Audit", "data": data},
    )


def seed_grievance_users(request):
    response = seed_database()
    return HttpResponse(response)


def ugc_compliance_page(request):
    hero_img = Hero_Image.objects.filter(page="ugc_compliance").first()
    gallery = Gallery.objects.all().order_by("?")[:6]

    return render(
        request,
        "Administration/ugc_compliance.html",  # 👈 Make sure path is correct
        context={
            "hero_img": hero_img,
            "hero_title": "UGC Compliance",
            "gallery": gallery,
        },
    )
def ugc_icc_page(request):
    hero_img = Hero_Image.objects.filter(page="ugc_icc").first()
    gallery = Gallery.objects.all().order_by("?")[:6]

    members = [
        {"name": "Dr Dhanya S", "designation": "Professor & Dean - Student Affairs", "phone": "", "role": "Chairperson"},
        {"name": "Dr Shiney Thomas", "designation": "Associate Professor, BS&H", "phone": "9446817255", "role": "Member"},
        {"name": "Ms. Asha Raj", "designation": "Assistant Professor, CSE", "phone": "9633291997", "role": "Member"},
        {"name": "Mr. Prisly Varghese Mathew", "designation": "Assistant Professor, ME", "phone": "9744891402", "role": "Member"},
        {"name": "Mr. Joseph Zacharia", "designation": "Librarian", "phone": "9947997767", "role": "Member"},
        {"name": "Mr. P K Binoy", "designation": "Lab Instructor, ME", "phone": "9446717178", "role": "Member"},
        {"name": "Ms. Parvathy Aravind", "designation": "Student (S8, CSE-A)", "role": "Student Member"},
        {"name": "Mr. Abhiraj Dinesh", "designation": "Student (S8, ME)", "role": "Student Member"},
        {"name": "Ms. Megha Suresh", "designation": "Student (S5, ECE)", "role": "Student Member"},
        {"name": "Ms. Sheela Baji", "designation": "People’s Council for Social Justice", "role": "NGO Member"},
    ]
    
    # Hardcoded minutes pointing to the static folder
    minutes = [
        {
            "title": "ICC review and planning of activities",
            "date": "27/11/2025",
            "file": {
                "url": static("pdfs/ICC minutes2.pdf")
            }
        },
        {
            "title": "ICC constitution cum first level of discussions",
            "date": "10/07/2025",
            "file": {
                "url": static("pdfs/ICC minutes1.pdf")
            }
        }
    ]

    return render(
        request,
        "Administration/ugc_icc.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Internal Complaints Commitee(ICC)",
            "gallery": gallery,
            "members": members,
            "minutes": minutes, 
        },
    )

def ugc_grievance_page(request):
    hero_img = Hero_Image.objects.filter(page="ugc_grievance").first()
    gallery = Gallery.objects.all().order_by("?")[:6]
    
    # === ADDED MINUTES FETCH ===
    minutes = MeetingMinutes.objects.filter(category="grievance").order_by('-date')

    return render(
        request,
        "Administration/ugc_grievance.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Student Grievance & Redressal Cell",
            "gallery": gallery,
            "minutes": minutes, # <--- Added to context
        },
    )

def ugc_antiragging_page(request):
    hero_img = Hero_Image.objects.filter(page="ugc_antiragging").first()
    gallery = Gallery.objects.all().order_by("?")[:6]
    
    # === ADDED MINUTES FETCH ===
    minutes = MeetingMinutes.objects.filter(category="anti_ragging").order_by('-date')

    return render(
        request,
        "Administration/ugc_antiragging.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Anti-Ragging Committee",
            "gallery": gallery,
            "minutes": minutes, # <--- Added to context
        },
    )

def ugc_eoc_page(request):
    hero_img = Hero_Image.objects.filter(page="ugc_eoc").first()
    gallery = Gallery.objects.all().order_by("?")[:6]  # optional, if used in the template
    
    # === ADDED MINUTES FETCH ===
    minutes = MeetingMinutes.objects.filter(category="eoc").order_by('-date')

    return render(
        request,
        "Administration/ugc_eoc.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Equal Opportunity Cell",
            "gallery": gallery,  # optional
            "minutes": minutes, # <--- Added to context
        },
    )

def ugc_sedg_page(request):
    hero_img = Hero_Image.objects.filter(page="ugc_sedg").first()
    gallery = Gallery.objects.all().order_by("?")[:6]  # optional, use only if gallery is in template
    
    # === ADDED MINUTES FETCH ===
    minutes = MeetingMinutes.objects.filter(category="sedg").order_by('-date')

    return render(
        request,
        "Administration/ugc_sedg.html",
        context={
            "hero_img": hero_img,
            "hero_title": "SEDG Cell",
            "gallery": gallery,  # optional
            "minutes": minutes, # <--- Added to context
        },
    )

def ugc_idp_page(request):
    hero_img = Hero_Image.objects.filter(page="ugc_idp").first()
    
    # === ADDED MINUTES FETCH ===
    minutes = MeetingMinutes.objects.filter(category="idp").order_by('-date')

    return render(
        request,
        "Administration/ugc_idp.html",  
        context={
            "hero_img": hero_img,
            "hero_title": "UGC IDP Document",
            "minutes": minutes, # <--- Added to context
        },
    )

def ugc_fee_page(request):
    hero_img = Hero_Image.objects.filter(page="ugc_fee").first()
    gallery = Gallery.objects.all().order_by("?")[:6]  # Optional

    return render(
        request,
        "Administration/ugc_fee.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Fee Refund Policy",
            "gallery": gallery,  # Optional
        },
    )

def committee_accessibility_page(request):
    hero_img = Hero_Image.objects.filter(page="committee_accessibility").first()
    gallery = Gallery.objects.all().order_by("?")[:6]
    
    # === ADDED MINUTES FETCH ===
    minutes = MeetingMinutes.objects.filter(category="accessibility").order_by('-date')
    
    return render(
        request,
        "Administration/committee_accessibility.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Committee for Accessibility Standards and Inclusive Practices",
            "gallery": gallery,
            "minutes": minutes, # <--- Added to context
        },
    )


def merit_admission_page(request):
    hero_img = Hero_Image.objects.filter(page="merit_admission").first()
    gallery = Gallery.objects.all().order_by("?")[:6]
    return render(request, "Administration/merit_admission.html",
            context={
        "hero_img": hero_img,
        "hero_title": "Merit Admission",
        "schedule_slots": MeritAdmissionScheduleSlot.objects.all(),
        "original_documents": MeritAdmissionDocument.objects.filter(type="original"),
        "copy_documents": MeritAdmissionDocument.objects.filter(type="copy"),
        "document_notes": MeritAdmissionDocumentNote.objects.all(),
        "bank_detail": MeritAdmissionBankDetail.objects.first(),
        "uniform_fee": MeritAdmissionUniformFee.objects.first(),
        "form_link": MeritAdmissionFormLink.objects.first(),
        "tutorial": MeritAdmissionTutorial.objects.first(),
        "general_contacts": MeritAdmissionContact.objects.filter(category="general"),
        "form_contacts": MeritAdmissionContact.objects.filter(category="form"),
    })


def mca_admission_page(request):
    hero_img = Hero_Image.objects.filter(page="admissions").first()
    return render(
        request,
        "Administration/mca_admission.html",
        context={
            "hero_img": hero_img,
            "hero_title": "MCA Admission",
        },
    )

def cpio_page(request):
    hero_img = Hero_Image.objects.filter(page="cpio").first()
    gallery = Gallery.objects.all().order_by("?")[:6]
    return render(request, "Administration/cpio.html", {
        "hero_img": hero_img,
        "hero_title": "Central Public Information Officer",
        "gallery": gallery,
    })

def audited_statements_page(request):
    hero_img = Hero_Image.objects.filter(page="audited_statements").first()

    return render(
        request,
        "Administration/audited_statements.html",  
        context={
            "hero_img": hero_img,
            "hero_title": "AUDITED STATEMENTS",
        },
    )

def exam_circulars_page(request):
    hero_img = Hero_Image.objects.filter(page="examination_cell").first()
    circulars = [
        {
            "title": "Examination Timetable for MBA S1 (R) Examination Dec. 2025",
            "date": "22/11/2025",
            "ref_no": "CCE/EX3/301/#1",
            "link": "https://drive.google.com/file/d/1SEynS0fiV0KZib24p-MuJ2np2NbRH4qP/view?usp=drivesdk" 
        },
        {
            "title": "Lab Examination Schedule for B. Tech S1 (R) Examination Nov. 2025",
            "date": "18/11/2025",
            "ref_no": "CCE/EX4/101/#1",
            "link": "https://drive.google.com/file/d/11uPCi7FJ-m4RsVVdRlzVuo4TdosXpHZM/view?usp=drivesdk"
        },
        {
            "title": "Examination Registrations for MBA S1 (R) Exam Dec 2025",
            "date": "17/11/2025",
            "ref_no": "CCE/EX2/301/#1",
            "link": "https://drive.google.com/file/d/1HGTOgyqykPNFU2neTC96VKCOPkGn1THS/view?usp=drivesdk"
        },
        { 
            "title": "Slot for MBA S1 (R) Examination Dec. 2025",
            "date": "14/11/2025",
            "ref_no": "CCE/EX1/301/#1",
            "link": "https://drive.google.com/file/d/1y7oePR_qUd-yo_pHOJm9y2nebHg8-ln_/view?usp=drivesdk"
        },
    ]

    return render(
        request,
        "Administration/exam_circulars.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Examination Circulars",
            "circulars": circulars,
        },
    )

def decennial_scholarship_page(request):
    hero_img = Hero_Image.objects.filter(page="decennial_scholarship").first()

    return render(
        request,
        "Administration/decennial_scholarship.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Decennial Scholarship",
        },
    )

def policies_page(request):
    hero_img = Hero_Image.objects.filter(page="policies").first()
    policies = Policy.objects.all()

    return render(
        request,
        "Administration/policies.html",
        context={
            "hero_img": hero_img,
            "hero_title": "Policies",
            "policies": policies,
        },
    )