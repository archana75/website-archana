from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home_page"),
    path('project/', views.project_page, name="project_page"),
    path('project/<int:id>', views.project_detail, name="project_detail")
]