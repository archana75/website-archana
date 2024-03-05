from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Project , Post, Event, Cms, Achievement, AchievementPhoto, Sliderimage
from django.utils.timezone import datetime

# Create your views here.
def index(request):
    top4_projects = Project.objects.all()[0:4]
    top8_projects = Project.objects.all().filter(school_product = True)[0:8]
    background_depan_judul = Cms.objects.get(name='bg_utama')
    background_student_project = Cms.objects.get(name='bg_project')
    bg_products = Cms.objects.get(name='bg_products')
    bg_header4 = Cms.objects.get(name='bg_header4')
    header_title = Cms.objects.get(name='header_title')
    sliderimages = Sliderimage.objects.all()
    

    today = datetime.today()
    events = Event.objects.filter(date_start__gte = today)

    return render(request, "main/index.html", {
                                'projects' : top4_projects,
                                'products' : top8_projects,
                                'events'   : events,
                                'bg_depan_judul': background_depan_judul,
                                'bg_depan_project': background_student_project,
                                'bg_products': bg_products,
                                'bg_header4': bg_header4,
                                'header_title' : header_title,
                                'sliderimages' : sliderimages,
                            })


def project_page(request):
    all_projects = Project.objects.filter(school_product = 0)
    return render(request, "main/project.html",{
        'projects' : all_projects,
    })

def project_detail(request, id):
    current_project = Project.objects.select_related("created_by").get(id=id)
    data = dict(
        project_title = current_project.title,
        project_description = current_project.description,
        project_image = current_project.image,
        project_logo = current_project.logo,
        project_attacment_link = current_project.attachment_link,
        project_video_link = current_project.video_link,
        user_firstname = current_project.created_by.firstname,
        user_lastname = current_project.created_by.lastname,
    )
    return render(request, "main/project_detail.html", data)
    
def products(request):
    all_products = Project.objects.filter(school_product = 1)
    backdrop = Cms.objects.get(name='background_judul')
    data = dict(products = all_products, background_judul = backdrop)
    return render(request, "main/products.html", data)

def future_events(request):
    all_events = Event.objects.all()
    data = dict(events = all_events)
    return render(request, "main/future_events.html", data)

def achievement(request):
    all_achievement = Achievement.objects.all()
    all_photos = AchievementPhoto
    data = dict(
            achievements = all_achievement,
            photos = all_photos,
            )
    return render(request, "main/achievement.html", data)

def achievement_detail(request, id):
    current_achievement = Achievement.objects.get(id=id)
    data = dict(
        achievement = current_achievement,

    )
    return render(request, "main/achievement_detail.html", data)
