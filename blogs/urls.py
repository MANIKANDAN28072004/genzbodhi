from django.urls import path, include
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blogView, name='blogUrl'),
    path('<slug:slug>', views.fullBlogView, name='fullBlogUrl'),
]