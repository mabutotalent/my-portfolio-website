from django.views.generic import ListView, DetailView

from . models import Project


class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    queryset = Project.objects.filter(active=True).order_by('project_title')


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
