from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Project , Post, Event, Cms, Achievement
from django.utils.timezone import datetime

# Create your views here.
def index(request):
    top4_projects = Project.objects.all()[0:4]
    top8_projects = Project.objects.all().filter(school_product = True)[0:8]
    bg_header = Cms.objects.get(name='bg_header')
    bg_header2 = Cms.objects.get(name='bg_header2')
    bg_header3 = Cms.objects.get(name='bg_header3')
    bg_header4 = Cms.objects.get(name='bg_header4')
    header_title = Cms.objects.get(name='header_title')

    today = datetime.today()
    events = Event.objects.filter(date_start__gt = today)

    return render(request, "main/index.html", {
                                'projects' : top4_projects,
                                'products' : top8_projects,
                                'events'   : events,
                                'bg_header': bg_header,
                                'bg_header2': bg_header2,
                                'bg_header3': bg_header3,
                                'bg_header4': bg_header4,
                                'header_title' : header_title,
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
    all_projects = Project.objects.filter(school_product = 1)
    data = dict(projects = all_projects)
    return render(request, "main/products.html", data)

def future_events(request):
    all_events = Event.objects.all()
    data = dict(events = all_events)
    return render(request, "main/future_events.html", data)

def achievement(request):
    all_achievement = Achievement.objects.all()
    data = dict(achievements = all_achievement)
    return render(request, "main/achievement.html", data)
