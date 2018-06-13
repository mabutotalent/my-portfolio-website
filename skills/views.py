from django.views.generic import ListView, DetailView

from . models import Skill


class SkillListView(ListView):
    template_name = 'skills/skill_list.html'
    context_object_name = 'skills'
    queryset = Skill.objects.all().order_by('-skill_name')
