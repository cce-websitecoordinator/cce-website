from django.shortcuts import render
from django.http import Http404, HttpResponse
from studentservices.models import *
import website.models
from website.models import Gallery, Hero_Image
from departments.models import NewsLetters,Magazines, ProfessionalBodies, ProfessionalBodiesEvents, ProfessionalBodiesTeamMembers
import aboutCCE.models


# Create your views here.
def arts_page(request):
    arts_updates = Artsupdates.objects.all()
    gallery_imgs = Gallery.objects.all().order_by('?')[:6]
    hero_img = Hero_Image.objects.all().filter(page="arts").first
    context = {'arts_updates':arts_updates,"events":ArtsEvents.objects.all(),"teams":artsTeamStatus.objects.all(),"gallery":gallery_imgs,"hero_img":hero_img,"hero_title":"Arts"}
    return render(request, 'StudentServices/arts.html',context=context)


 
def sports_page(request):
    arts_updates = SportsUpdates.objects.all()
    gallery_imgs = Gallery.objects.all().order_by('?')[:6]
    events = SportsEvents.objects.all()
    teams = SportsTeamStatus.objects.all()
    hero_img = Hero_Image.objects.all().filter(page="sports").first
    context = {'arts_updates':arts_updates,"events":events,"teams":teams,"gallery":gallery_imgs,"hero_img":hero_img,"hero_title":"Sports"}
    return render(request, 'StudentServices/sports.html',context=context)

def nss_page(request):
    about = NssAbout.objects.first
    members = NSSMembers.objects.all().order_by('priority')
    events = NssEvents.objects.all() 
    gallery_imgs = NssGallery.objects.all()
    hero_img = Hero_Image.objects.all().filter(page="nss").first
    context = {'about':about,'members':members,"events":events,"gallery":gallery_imgs,"hero_title":"NSS","hero_img":hero_img}
    return render(request, 'StudentServices/nss.html',context=context)

def iic_page(request):
    hero_img = Hero_Image.objects.all().filter(page="iic").first
    members = IICCommitee.objects.all()
    certificates = IICCertificate.objects.all()
    return render(request, 'StudentServices/iic.html',context={"hero_img":hero_img,"hero_title":"Institution’s Innovation Council","members":members,"certificates":certificates})


def womencell_page(request):
    data = WomenCellCommitee.objects.all()
    events = WomenEvents.objects.all()
    hero_img = Hero_Image.objects.all().filter(page="womencell").first
    return render(request, 'StudentServices/womencell.html',context={"data":data,"events":events,"hero_img":hero_img,"hero_title":"Women Empowerment Cell"})

def ieee_page(request):
    about = IEEEAbout.objects.all().first()
    events = IEEEevents.objects.all().order_by('-date')
    members = IEEEmembers.objects.all().order_by('priority')
    hero_img = Hero_Image.objects.all().filter(page="ieee").first()
    gallery = Gallery.objects.all().order_by('?')[:20]
    return render(request, 'StudentServices/ieee.html',context={"about":about,"hero_img":hero_img,"hero_title":"IEEE","events":events,"members":members,"gallery":gallery})


def pmi_page(request):
    slug = '8'
    context = {
        "professional_body": ProfessionalBodies.objects.filter(id=slug).first(),
        "events": ProfessionalBodiesEvents.objects.filter(ProfessionalBodies_id=slug),
        "members": ProfessionalBodiesTeamMembers.objects.filter(
            ProfessionalBodies_id=slug
        ).order_by("priority"),
        "gallery": website.models.Gallery.objects.all().order_by("?")[:6],
    }
    return render(
        request, "Departments/professsionalbody_showcase.html", context=context
    )

def union_page(request):
    union = Union.objects.all().first()
    union_members = UnionCommitee.objects.all()
    hero_img = Hero_Image.objects.all().filter(page="college_union").first
    return render(request, 'StudentServices/union.html',context={"union":union,"hero_img":hero_img,"hero_title":union.name,'union_members':union_members})

def techies_park_page(request):
    hero_img = Hero_Image.objects.filter(page="techies_park").first()
    
    return render(request,'StudentServices/techies_park.html',context={'hero_img':hero_img,'hero_title':'Techies Park'})

def study_abroad_page(request):
    hero_img = Hero_Image.objects.filter(page="study_abroad").first()
    
    return render(request,'StudentServices/study_abroad.html',context={'hero_img':hero_img,'hero_title':'Study Abroad'})


def mentoring_page(request):
    hero_img = Hero_Image.objects.all().filter(page="mentoring").first
    context_temp = {
        'title': 'Mentoring',
        'hero_title': 'Mentoring',
        'hero_img':hero_img,
    }

    about = Mentoring.objects.all().first()
    events = MentoringEvents.objects.all().order_by("-date")
    members = MentoringTeam.objects.all()
    gallery = Gallery.objects.all()

    context={**context_temp,"about":about,"events":events,"members":members,"gallery":gallery}

    return render(request, 'StudentServices/mentoring.html',context=context)

def irc_page(request):
    hero_img = Hero_Image.objects.all().filter(page="international_relations").first
    context_temp = {
        'title': 'International Relations Cell',
        'hero_title': 'International Relations Cell',
        'hero_img': hero_img,
    }
    about = IRCAbout.objects.all().first()
    events = IRCEvents.objects.all()
    members = IRCTeam.objects.all().order_by('priority')


    context={**context_temp,"about":about,"events":events,"members":members}
    return render(request, 'StudentServices/irc.html',context=context)

def ccil_page(request):
    hero_img = Hero_Image.objects.all().filter(page="ccil").first
    context_temp = {
        'title': 'Christ Center for Innovation and Open Learning',
        'hero_title': 'Christ Center for Innovation and Open Learning',
        'hero_img': hero_img,
    }
    about = CCILAbout.objects.all().first()
    events = CCILEvents.objects.all()
    sepgallery = CCILGallery.objects.all()
    members = CCILTeam.objects.all().order_by('priority')
    gallery = Gallery.objects.all().order_by('?')[:20]


    context={**context_temp,"about":about,"events":events,"members":members,"gallery":gallery,"sepgallery":sepgallery}
    return render(request, 'StudentServices/ccil.html',context=context)

def ccevr_page(request):
    context_temp = {
        'title': 'Christ Center for Electric Vehicle Research',
        'hero_title': 'Christ Center for Electric Vehicle Research',
        'hero_img': Hero_Image.objects.filter(page='ccevr').first(),
    }
    about = CCEVRAbout.objects.all().first()
    events = CCEVREvents.objects.all()
    members = CCEVRTeam.objects.all().order_by('priority')
    gallery = Gallery.objects.all().order_by('?')[:20]


    context={**context_temp,"about":about,"events":events,"members":members,"gallery":gallery}
    return render(request, 'StudentServices/ccevr.html',context=context)


def central_library_page(request,slug):  # sourcery skip: extract-method
    context_temp = {
        'title': 'Central Library',
        'hero_title': 'Central Library',
        'hero_img': Hero_Image.objects.filter(page='library').first(),
        'route': slug,
    }
    context={**context_temp}
    match slug:
        case 'central_library':
            vision = CentralLibrary.objects.filter(name='Vision').first()
            mission = CentralLibrary.objects.filter(name='Mission').first()
            about = CentralLibrary.objects.filter(name="about").first() 
            img = LibraryImages.objects.all()
            gallery = Gallery.objects.all().order_by('?')[:6]
            context = {**context_temp,'vision':vision,'mission':mission,'about':about,"gallery":gallery,"img":img}
            return render(request, 'StudentServices/central_library.html',context=context)
        case "faculty_and_staff":
            context = {**context_temp,'data':LibraryFaculty.objects.all()}
            return render(request, 'StudentServices/faculty_and_staff.html',context=context)
        case "library_info":
            data = LibraryInfo.objects.all()
            context = {'data':data,**context_temp}
            return render(request, 'StudentServices/library_info.html',context=context)
        case "rules_and_regulations":
            return render(request, 'StudentServices/rules_and_regulations.html',context=context)
        case "digital_library":
            context = {**context_temp,'data':DigitalLibrary.objects.all()}
            return render(request, 'StudentServices/digital_library.html',context=context)
        case "ieee_journals":
            journals = IEEEJournals.objects.all()
            context = {**context_temp,"journals":journals}
            return render(request, 'StudentServices/ieee_journals.html',context=context)
        case "newsletters":
            context = {**context_temp,'data':NewsLetters.objects.all(),"data1":Magazines.objects.all(),"college_data":aboutCCE.models.CollegeMagazine.objects.all()}
            return render(request, 'StudentServices/newsletter.html',context=context)
        
            
def clubs_page(request,slug):
    club_names = [club[0] for club in Clubs.objects.all().values_list('name')]
    context_temp = {
        
        'route': slug,
        'gallery':Gallery.objects.all().order_by('?')
    }
    context={**context_temp}
    if slug == "index":
        data = Clubs.objects.all()
        hero_img = Hero_Image.objects.filter(page="clubs").first()
        context = {**context_temp,"data":data,"hero_title":"Clubs","hero_img":hero_img}
        return render(request, 'StudentServices/clubs/index.html',context=context)
    elif slug in club_names:
        club = Clubs.objects.filter(name=slug).first()
        events = ClubEvents.objects.all().filter(club__name = slug).order_by('-date')
        members = ClubMembers.objects.all().filter(club__name = slug).order_by('priority')
        hero_img = ClubsHeroImage.objects.filter(club__name = slug).first()
        context = {**context_temp,"club":club,"hero_title":club.name,"events":events,"members":members,"hero_img":hero_img}
        return render(request, 'StudentServices/clubs/club_template.html',context=context)
    else:
        return Http404("Page Not Found")
        