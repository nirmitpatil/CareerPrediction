from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import *
from Career.models import Tests
from Career.models import General_Test
from django.http import HttpResponse


def resume(request):
    return render(request , 'Resumes.html')
def resume1(request):
    return render(request , '1.html')
def resume2(request):
    return render(request , '2.html')
def resume3(request):
    return render(request , '3.html')
def resume4(request):
    return render(request , '4.html')
def resume5(request):
    return render(request , '5.html')