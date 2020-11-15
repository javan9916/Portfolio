from typing import ContextManager
from django.shortcuts import render
from app.models import Project

####### global variables #########
me_img1 = 'img/me1.jpg'         ##
me_img2 = 'img/me2.jpg'         ##
style = 'styles/styles.css'     ##
##################################

def home(request):
    projects = Project.objects.all()
    context = {
        'home_page': 'active',
        'main_img': me_img1,
        'styles': style,
        'projects': projects
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'about_page': 'active',
        'main_img': me_img2,
        'styles': style,
    }
    return render(request, 'about.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects_page': 'active',
        'styles': style,
        'projects': projects
    }
    return render(request, 'projects.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
        'styles': style
    }
    return render(request, 'project_detail.html', context)