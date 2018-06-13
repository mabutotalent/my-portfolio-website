from django.urls import path

from . import views

app_name = 'skills'

urlpatterns = [
    path('list/', views.SkillListView.as_view(), name='skill-list'),
    ]
