from django.shortcuts import render
from . import forms

# Create your views here.
def blogView(request):
    return render(request, 'blog.html')

def fullBlogView(request, slug):
    return render(request, 'fullBlog.html')

def postFormView(request):
    context = {}
    if request.method == "POST":
        pass
    context['form'] = forms.postform()
    return render(request, 'postform.html', context)
