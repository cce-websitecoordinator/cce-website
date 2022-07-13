from django.shortcuts import render



def home_page(request):
    context = {'Testimonials': [
        {'name': 'John Doe',
         'role': 'Student',
         'department': 'Department Of Electrical and Electrical Engineering',
         'quote': ' A set of words that is complete in itself, typically containing a subject and predicate, conveying a statement, question, exclamation, or command. ',
         'image': 'https://www.w3schools.com/howto/img_avatar.png',
         'batch': '2019-2020'},


        {'name': 'John Doe',
         'role': 'Student',
         'department': 'Department Of Electrical and Electrical Engineering',
         'quote': 'I am a student of Electrical and Electrical Engineering at the University of Pretoria. I am a very active student and I am very happy to be a part of the team that is working on the website.',
         'image': 'https://www.w3schools.com/howto/img_avatar2.png',
         'batch': '2019-2020'},
    ], "name": "John Doe", }
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
    return render(request, 'nirf.html')

def gallery_page(request):
    return render(request, 'gallery.html')