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


def departments_page(request):
    return render(request, 'departments.html')


def campuslife_page(request):
    return render(request, 'campuslife.html')


def about_page(request):
    return render(request, 'about.html')

def nirf_page(request):
    return render(request, 'nirf.html')

def gallery_page(request):
    return render(request, 'gallery.html')