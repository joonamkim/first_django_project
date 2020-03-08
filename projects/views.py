from django.shortcuts import render
from projects.models import Project


# Create your views here.
# rendering data functions to specified html files

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def blog_index(request):
    return render(request, 'blog_index.html')
