from django.shortcuts import render

# Create your views here.
def blogView(request):
    return render(request, 'blog.html')

def fullBlogView(request, slug):
    return render(request, 'fullBlog.html')
