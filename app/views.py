from typing import ContextManager
from django.shortcuts import render
from app.models import Project

me_img1 = 'img/me1.jpg'
me_img2 = 'img/me2.jpg'

def home(request):
    projects = Project.objects.all()
    
    style = 'styles/styles.css'
    context = {
        'home_page': 'active',
        'main_img': me_img1,
        'styles': style,
        'projects': projects
    }
    return render(request, 'home.html', context)

def about(request):
    style = 'styles/styles.css'
    context = {
        'about_page': 'active',
        'main_img': me_img2,
        'styles': style,
    }
    return render(request, 'about.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)