from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User 
from django.contrib import messages
from . import models

# Create your views here.

def register(request):
        
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if(password == password2):
            if User.objects.filter(email=email).exists():
                messages.info(request, 'EMAIL ALREADY EXIST!!!')
                return redirect('profiles:register')    
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'USERNAME ALREADY EXIST!!!')
                return redirect('profiles:register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                profile = models.profiles(user=user)
                profile.save()
                return redirect('profiles:login')
        else:
            messages.info(request, 'INVALID PASSWORD!!!')
            return redirect('profiles:register')   
    else:     
        return render(request, 'register.html')
    
def login(request):
    if(request.method == "POST"):
        
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user:
            auth.login(request,user)
            return redirect("feeds:home")
        else:
            messages.info(request, 'INVALID CREDENTIALS!!')
            return redirect('profiles:login')


    else:    
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect("/")