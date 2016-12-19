from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import permalink

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,null=True)
    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('category_list', None, { 'slug': self.slug })

class Entry(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    link = models.URLField(max_length=200, blank=True)
    short_description = models.CharField(max_length=600)
    technologies = models.CharField(max_length=200)

    @permalink
    def get_absolute_url(self):
        return('entry_detail',None, {'entry_slug':self.slug})

    def __str__(self):
        return self.title
