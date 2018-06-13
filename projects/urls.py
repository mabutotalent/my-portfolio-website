from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('list/', views.ProjectListView.as_view(), name='project-list'),
    path('<slug:slug>', views.ProjectDetailView.as_view(), name='project-detail'),
]
