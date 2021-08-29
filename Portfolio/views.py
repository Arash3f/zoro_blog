from django.shortcuts import get_object_or_404, render
from Account import models
from Project.models import Project
from Paper.models import My_Papers
from taggit.models import Tag

def Portfolio_page(request):
    html = 'Portfolio/portfolio.html'
    user        = get_object_or_404(models.User,id=1)
    skills      = models.Skill.objects.all().order_by('-amount')
    experiences = models.Experience.objects.all().order_by('-Date')
    tags        = Tag.objects.all()
    services    = models.Service.objects.all()[:3]
    projects    = Project.objects.all()[:6]
    papers    = My_Papers.objects.all()[:6]
    
    data = {    'user'  :user ,
                'skills' :skills , 
                'exps'   :experiences ,
                'projs' :projects ,
                'papers' :papers ,
                'tags' :tags ,
                'services' : services
            }
    
    return render(request,html,data)

def about_page(request):
    html = 'Portfolio/about.html'
    user        = get_object_or_404(models.User,id=1)
    skills      = models.Skill.objects.all().order_by('-amount')
    
    data = {    'user'  :user ,
                'skills' :skills 
            }
    
    return render(request,html,data)
