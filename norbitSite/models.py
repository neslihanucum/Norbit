from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Post(models.Model):
    first_name = models.CharField(max_length=255, default='admin')
    last_name = models.CharField(max_length=255, default='admin')
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_image/%Y/%m/%d/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {self.author}"


    def get_absolute_url(self):
        return reverse('norbitSite:index')