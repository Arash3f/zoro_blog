from django.shortcuts import get_object_or_404, render
from Project.models import Project
from django.db.models import Q
from django.views.generic.list import ListView

def project_detail(request,slug):
    another_projects = Project.objects.filter(~Q(slug=slug))[:5]
    project = get_object_or_404(Project, slug=slug )
    data = {    'project'  :project ,
                'another_projects' :another_projects 
            }  
    return render(request, 'Project/project_details.html' , data)

class project_list(ListView):
    template_name = 'Project/projects.html'
    model = Project

    def get_success_url(self):
        return ''