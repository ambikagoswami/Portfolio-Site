from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def skills(request):
    return render(request,'skills.html')

def projects(request):
    return render(request,'projects.html')

def intern(request):
    return render(request,'intern.html')

def contacts(request):
    return render(request,'contacts.html')

