from django.db import models
from django.urls import reverse

# Create your models here.


class Project(models.Model):

    creation_date = models.DateField(auto_now=True)
    publication_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=False)
    project_title = models.CharField(max_length=250)
    project_description = models.TextField(blank=True)
    project_url = models.URLField(blank=True, null=True)
    last_viewed = models.DateTimeField()
    slug = models.SlugField()

    def __str__(self):
        return self.project_title

    def get_absolute_url(self):
        return reverse('projects:project-detail', kwargs={"slug": self.slug, })
