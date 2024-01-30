from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home_page"),
    path('project/', views.project_page, name="project_page"),
    path('project/<int:id>', views.project_detail, name="project_detail"),
    path('products/', views.products, name="products"),
    path('future_events/', views.future_events, name="future_events"),
    path('achievement/', views.achievement, name="achievement"),
    path('achievement/<int:id>', views.achievement_detail, name="achievement_detail"),
    
]