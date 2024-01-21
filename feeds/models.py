from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class post(models.Model):
    textContent = models.TextField()
    imageContent = models.ImageField(upload_to='post', null=True)
    postedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    postedOn = models.DateTimeField(default=datetime.now(), blank=True)

    class Meta:
        ordering = ['-postedOn']
