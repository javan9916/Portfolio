from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('<int:pk>/', views.project_detail, name='project_detail')
]