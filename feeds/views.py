from django.shortcuts import render, redirect
from . import models
from profiles import models as profilemodels
from . import forms


# Create your views here.

def home(request):
    userId = request.user.id
    posts = models.post.objects.all()
    profiles = profilemodels.profiles.objects.all()
    context = {'posts': posts, 'profiles':profiles}
    return render(request, 'feeds.html', context)

def postform(request):
    context = {}
    user = request.user
    if request.method == "POST":
        form = forms.postform(request.POST, request.FILES)
        if form.is_valid():
            textContent = form.cleaned_data.get('text')
            imageContent = form.cleaned_data.get('image')
            obj = models.post.objects.create(textContent = textContent, 
                                             postedBy = user,
                                             imageContent = imageContent)
            obj.save()
            return redirect('feeds:home')
    context['form'] = forms.postform()
    return render(request, 'postform.html', context)

