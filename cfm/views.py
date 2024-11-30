from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from .models import *

def home(request):
    homeSliders = HomepageSliders.objects.all()
    homesections = HomeSections.objects.all()
    sermons = Sermons.objects.all().order_by('-date')[:3]

    context = {
        'homeSliders': homeSliders,
        'homesections': homesections,
        'sermons': sermons
    }
    return render(request, 'home.html', context)


def about_us(request):

    
    return render(request, 'about.html')

def contactus(request):

    
    return render(request, 'contactus.html')

def solution(request, *args, **kwargs):
    url_name = kwargs['slug']
    
    return render(request, 'solution.html')


def give(request):
    
    return render(request, 'give.html')


def contactus(request):
    return render(request, 'contactus.html')

def gallery(request, *args, **kwargs):

    cat = kwargs['cat']
    
    if cat == 'all':
        all_images = Gallery.objects.all()
    else:
        all_images = Gallery.objects.filter(category=cat.lower())
    context = {
        'all_images':all_images,
    }
    return render(request, 'gallery.html', context)

def events(request):
    all_events = Events.objects.all()
    context = {
        'all_events': all_events
    }
    return render(request, 'events.html', context)


def sermons(request, *args, **kwargs):
    cat = kwargs['cat']

    if cat == 'all':
        all_sermons = Sermons.objects.all()
    else:
        all_sermons = Sermons.objects.filter(category=cat.lower())
    context = {
        'all_sermons': all_sermons
    }
    return render(request, 'sermons.html', context)


def signin(request):

    
    return render(request, 'login.html')


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)