from django.shortcuts import render
from website.models import *


def home_page(request):
    context = {'Testimonials': Testimonials.objects.all().values(), "name": "John Doe","updates":HomeUpdates.objects.all().values(),"Events":HomeEvents.objects.all().values(),"gallery":Gallery.objects.all().values()}
    return render(request, 'home.html', context=context)


def academics_page(request):

    return render(request, 'academics.html')


def department_of_BSH_page(request):
    context={
    "Page_Title": 
        "Basic Sciences and Humanities",
    "About_Data":
        "Department of Computer Science & Engineering started in 2015 in Christ College of Engineering, which offers the undergraduate (B. Tech.) course. The annual intake of the B. Tech. program is 60 students and it is affiliated to Dr. A P J Abdul Kalam Technological University. The department provides the students an environment that stimulates their intellectual growth and personality development. We provide excellent infrastructure facilities with well-equipped computer labs, smart classrooms, digital library and language lab. We also have high speed leased line Internet connection and online access to all IEEE journals. The Department has an excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research.",
    "Vision":
        "Vision excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Mission":
        "excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Values":
        "excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Hero_image":
        "../../static/images/BSH_Department.png",
    "Department_Abbrevation":
        "BSH"
    }
    return render(request, 'Departments/index.html',context=context)

def department_of_CSE_page(request):
    context={"Page_Title": "Computer Science and Engineering",
    "About_Data":
        "Department of Computer Science & Engineering started in 2015 in Christ College of Engineering, which offers the undergraduate (B. Tech.) course. The annual intake of the B. Tech. program is 60 students and it is affiliated to Dr. A P J Abdul Kalam Technological University. The department provides the students an environment that stimulates their intellectual growth and personality development. We provide excellent infrastructure facilities with well-equipped computer labs, smart classrooms, digital library and language lab. We also have high speed leased line Internet connection and online access to all IEEE journals. The Department has an excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research.",
    "Vision":
        "Vision excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Mission":
        "excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Values":
        "excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Hero_image":
        "../../static/images/CSE_Department.png",
    "Department_Abbrevation":
        "CSE"}
    return render(request, 'Departments/index.html',context=context)

def department_of_CE_page(request):
    context={"Page_Title": "Civil Engineering",
    "About_Data":
        "Department of Computer Science & Engineering started in 2015 in Christ College of Engineering, which offers the undergraduate (B. Tech.) course. The annual intake of the B. Tech. program is 60 students and it is affiliated to Dr. A P J Abdul Kalam Technological University. The department provides the students an environment that stimulates their intellectual growth and personality development. We provide excellent infrastructure facilities with well-equipped computer labs, smart classrooms, digital library and language lab. We also have high speed leased line Internet connection and online access to all IEEE journals. The Department has an excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research.",
    "Vision":
        "Vision excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Mission":
        "excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Values":
        "excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Hero_image":
        "../../static/images/CE_Department.png",
    "Department_Abbrevation":
        "CE"}
    return render(request, 'Departments/index.html',context=context)

def department_of_ME_page(request):
    context={"Page_Title": "Mechanical Engineering",
    "About_Data":
        "Department of Computer Science & Engineering started in 2015 in Christ College of Engineering, which offers the undergraduate (B. Tech.) course. The annual intake of the B. Tech. program is 60 students and it is affiliated to Dr. A P J Abdul Kalam Technological University. The department provides the students an environment that stimulates their intellectual growth and personality development. We provide excellent infrastructure facilities with well-equipped computer labs, smart classrooms, digital library and language lab. We also have high speed leased line Internet connection and online access to all IEEE journals. The Department has an excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research.",
    "Vision":
        "Vision excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Mission":
        "excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Values":
        "excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Hero_image":
        "../../static/images/ME_Department.png",
    "Department_Abbrevation":
        "ME"}
    return render(request, 'Departments/index.html',context=context)

def department_of_EEE_page(request):
    context={"Page_Title": "Electrical and Electronics Engineering",
    "About_Data":
        "Department of Computer Science & Engineering started in 2015 in Christ College of Engineering, which offers the undergraduate (B. Tech.) course. The annual intake of the B. Tech. program is 60 students and it is affiliated to Dr. A P J Abdul Kalam Technological University. The department provides the students an environment that stimulates their intellectual growth and personality development. We provide excellent infrastructure facilities with well-equipped computer labs, smart classrooms, digital library and language lab. We also have high speed leased line Internet connection and online access to all IEEE journals. The Department has an excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research.",
    "Vision":
        "Vision excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Mission":
        "excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Values":
        "excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research"
        ,
    "Hero_image":
        "../../static/images/EEE_Department.png",
    "Department_Abbrevation":
        "EEE"}
    return render(request, 'Departments/index.html',context=context)

def department_of_ECE_page(request):
    context={"Page_Title": "Electronics and Communication Engineering",
    "About_Data":
        "Department of Computer Science & Engineering started in 2015 in Christ College of Engineering, which offers the undergraduate (B. Tech.) course. The annual intake of the B. Tech. program is 60 students and it is affiliated to Dr. A P J Abdul Kalam Technological University. The department provides the students an environment that stimulates their intellectual growth and personality development. We provide excellent infrastructure facilities with well-equipped computer labs, smart classrooms, digital library and language lab. We also have high speed leased line Internet connection and online access to all IEEE journals. The Department has an excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research.",
    "Vision":
        "Vision excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Mission":
        "excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Values":
        "excellent team of committed and qualified faculty members encouraging and guiding students in their academic as well as personal development. We pride ourselves in providing a positive environment conducive to Engineering Studies and Research",
    "Hero_image":
        "../../static/images/ECE_Department.png",
    "Department_Abbrevation":
        "ECE"}
    return render(request, 'Departments/index.html',context=context)


def campuslife_page(request):
    return render(request, 'campuslife.html')


def about_page(request):
    return render(request, 'about.html')

def nirf_page(request):
    return render(request, 'nirf.html',context={})

def gallery_page(request):
    return render(request, 'gallery.html')

def iqac_page(request):
    return render(request, 'iqac.html')


def test_page(request):
    return render(request, 'Test.html')


def server_error_page(request):
    return render(request, 'Errors/500.html')

def not_found_error_page(request,exception):
    return render(request, 'Errors/404.html')
