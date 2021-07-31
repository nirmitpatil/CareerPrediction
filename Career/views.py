from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import *
from .models import Tests
from .models import General_Test
from .models import Advance_Test
from .models import College
from .models import Review
from django.http import HttpResponse
from django.db import connection
#import fusioncharts
# Create your views here.
def home(request):
    test =General_Test.objects.all()
    return render(request , 'home.html',{'test':test})
def about(request):
    return render(request , 'about.html')

score=0

def iq(request):
    test =Tests.objects.all()
    return render(request , 'iq.html', {'test':test})

def general_func(request):
    test =General_Test.objects.all()
    sci=0
    com=0
    art=0
    for t in test:
        answer=t.Answer
        ans=request.POST.get(str(t.i))
        if answer == ans:
            if t.Test_Id == 1:
                sci=sci+1
            if t.Test_Id == 2:
                com=com+1
            if t.Test_Id == 3:
                art=art+1

    if (sci >= com) and (sci >= art):
        max = "SCIENCE"
        max1 = 1
    elif (com >= sci) and (com >= art):
        max = "COMMERCE"
        max1 = 2
    else:
        max = "ARTS"
        max1 = 3

    max2 = Advance_Test.objects.filter(Test_Section=max1)
    return render(request , 'general_test.html',{'suggested':max,'test':max2,'test_section':max1})

def advance_func(request):
    fil=request.POST.get('test_section')
    test =Advance_Test.objects.filter(Test_Section=fil)
    a=0
    b=0
    c=0
    d=0
    if fil == "1":
        for t in test:
            answer=t.Answer
            ans=request.POST.get(str(t.id))
            if answer == ans:
                if t.Test_Id == 1:
                    a=a+1
                if t.Test_Id == 2:
                    b=b+1
                if t.Test_Id == 3:
                    c=c+1
                if t.Test_Id == 4:
                    d=d+1

        if((a>=b) and (a>=c) and (a>=d)):
            max = "Engineering"
            max1 = 1
        elif((b>=a) and (b>=c) and (b>=d)):
            max = "Pharmacy"
            max1 = 2
        elif((c>=a) and (c>=b) and (c>=d)):
            max = "MBBS"
            max1 = 3
        elif((d>=a) and (d>=b) and (d>=c)):
            max = "BSC"
            max1 = 4

    if fil == "2":
        for t in test:
            answer=t.Answer
            ans=request.POST.get(str(t.id))
            if answer == ans:
                if t.Test_Id == 1:
                    a=a+1
                if t.Test_Id == 2:
                    b=b+1
                if t.Test_Id == 3:
                    c=c+1
                if t.Test_Id == 4:
                    d=d+1

        if((a>=b) and (a>=c) and (a>=d)):
            max = "LLB"
            max1 = 5
        elif((b>=a) and (b>=c) and (b>=d)):
            max = "BBA"
            max1 = 6
        elif((c>=a) and (c>=b) and (c>=d)):
            max = "BMM"
            max1 = 7
        elif((d>=a) and (d>=b) and (d>=c)):
            max = "BCOM"
            max1 = 8
    if fil == "3":
        for t in test:
            answer=t.Answer
            ans=request.POST.get(str(t.id))
            if answer == ans:
                if t.Test_Id == 1:
                    a=a+1
                if t.Test_Id == 2:
                    b=b+1
                if t.Test_Id == 3:
                    c=c+1
                if t.Test_Id == 4:
                    d=d+1

        if((a>=b) and (a>=c) and (a>=d)):
            max = "BA"
            max1 = 9
        elif((b>=a) and (b>=c) and (b>=d)):
            max = "BHM OR BEM"
            max1 = 10
        elif((c>=a) and (c>=b) and (c>=d)):
            max = "BA+LLB"
            max1 = 11
        elif((d>=a) and (d>=b) and (d>=c)):
            max = "BFA"
            max1 = 12
    
    
    max2 = College.objects.filter(section=max1)
    return render(request , 'advance_test.html',{'suggested':max,'col':max2})

def review_display(request, C_id):
    #ans=request.GET.get("C_id")
    ans2 = Review.objects.filter(C_id=C_id)
    ans = College.objects.filter(id=C_id)
    return render(request , 'reviews.html',{'col1':ans2,'col':ans})

def iq_func(request):
    test =Tests.objects.all()
    count=0
    for t in test:
        answer=t.Answer
        ans=request.POST.get(str(t.id))
        if answer == ans:
            count=count+1
    if count <= 0:
        aa=0
    elif count <= 1:
        aa=60
    elif count <= 2:
        aa=70
    elif count <= 3:
        aa=80
    elif count <= 4:
        aa=90
    elif count <= 5:
        aa=100
    elif count <= 6:
        aa=110
    elif count <= 7:
        aa=120
    elif count <= 8:
        aa=130
    elif count <= 9:
        aa=140
    elif count <= 10:
        aa=150
    return render(request , 'iq_test.html', {'count':aa})
