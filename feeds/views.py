from django.shortcuts import render
from . import models
from . import forms


# Create your views here.

def home(request):
    userId = request.user.id
    post = models.post.objects.all()
    context = {'posts': post}
    return render(request, 'feeds.html', context)

def postform(request):
    context = {}
    if request.method == "POST":
        pass
    context['form'] = forms.postform()
    return render(request, 'postform.html', context)

