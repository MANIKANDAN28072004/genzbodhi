from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def blogView(request):
    context = dict()
    blogs = models.Blog.objects.all()
    context['blogs'] = blogs
    print(blogs)
    return render(request, 'blog.html', context)

def fullBlogView(request, slug):
    context = {}
    blogs = models.Blog.objects.get(blogSlug=slug)
    context['blog'] = blogs
    
    return render(request, 'fullBlog.html', context)

def postFormView(request):
    context = {}
    user = request.user
    if request.method == "POST":
        form = forms.postform(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            heading = form.cleaned_data.get('heading')
            textContent = form.cleaned_data.get('text')
            imageContent = form.cleaned_data.get('image')
            obj = models.Blog.objects.create(heading=heading,
                                            textContent = textContent, 
                                             postedBy = user,
                                             imageContent = imageContent)
            obj.save()
            return redirect('feeds:home')
    context['form'] = forms.postform()
    return render(request, 'postform.html', context)
