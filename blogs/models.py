from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    heading = models.CharField(max_length=200)
    textContent = models.TextField()
    blogSlug = models.SlugField(unique=True)
    imageContent = models.ImageField(upload_to='post', null=True)
    postedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    postedOn = models.DateTimeField(default=datetime.now(), blank=True)

    def save(self, *args, **kwargs):  # new
        if not self.blogSlug:
            self.blogSlug = slugify(self.heading)
        return super().save(*args, **kwargs)