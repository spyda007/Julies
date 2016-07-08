from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, loader
from .models import Course, PersonalDetails,Choices
from django.conf.urls import url

def index(request):
    return render(request, "index.html", {})

def course(request):
	return render(request, "course.html",{})

def personaldetails(request):
	return render(request, "personal.html", {})

def choices(request):
	return render(request, "apply2.html", {})

def login(request):
	return render(request, "login.html", {})

def courses2(request):
	return render(request, "course2.html",{})

#	return render(request, "course.html")
# Create your views here.
