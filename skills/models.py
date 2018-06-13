from django.db import models
from django.urls import reverse

# Create your models here.


class Skill(models.Model):
    """Class for individual skills."""

    skill_name = models.CharField(max_length=100)
    skill_level = models.TextField(blank=True)
    skill_category = models.ForeignKey('SkillCategory', on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.skill_name


class SkillCategory(models.Model):
    """Class for skill categories, grouping skills."""

    category_name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'SkillCategories'

    def __str__(self):
        return self.category_name
