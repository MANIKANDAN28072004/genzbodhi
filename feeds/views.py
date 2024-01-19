from django.shortcuts import render
from . import models


# Create your views here.

def home(request):
    post = models.post.objects.all()
    context = {'posts': post}
    return render(request, 'feeds.html', context)
