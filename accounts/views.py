from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import *
from Career.models import Tests
from Career.models import General_Test
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method== 'POST':
        username=request.POST.get('username',False)
        password=request.POST.get('password',False)

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            test =General_Test.objects.all()
            return render(request , 'home.html',{'test':test})
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request , 'login.html')

def signup(request):

    if request.method == 'POST':
        
        first_name=request.POST.get('first_name',False)
        last_name=request.POST.get('last_name',False)
        username=request.POST.get('username',False)
        password1=request.POST.get('password1',False)
        password2=request.POST.get('password2',False)
        email=request.POST.get('email',False)

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matched')
            return redirect('signup')
        return redirect('/')
    
    else:
        return render(request , 'signup.html')



def logout(request):
    auth.logout(request)
    return render(request , 'login.html')
