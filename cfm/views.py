from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from .models import *

def home(request):
    if request.method == 'POST':
        # Retrieve form data
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cartons = request.POST.get('cartons')
        message = request.POST.get('message')

        # Build email content
        email_content = f'Dear Admin,\n\n'
        email_content += f'New User reached out!\n'
        email_content += f'Name: {user_name}\n'
        email_content += f'Email: {email}\n'
        email_content += f'Phone: {phone}\n'
        email_content += f'Number of Cartons/week: {cartons}\n'
        email_content += f'Message: {message}\n\n'
        email_content += f'Please respond as soon as possible.\n\n'

        try:
                send_mail(
                    subject='New Inquiry',
                    message=email_content,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['mail@christfm.orgng.com'],  
                    fail_silently=False,
                )
               
                print("Email sent successfully!")  
        except BadHeaderError as e:
                print(f"Error sending email: {e}")

    homeSliders = HomepageSliders.objects.all()
    homesections = HomeSections.objects.all()
    sermons = Sermons.objects.all().order_by('-date')[:3]
    # print(homeSliders.values())

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



def register(request):
    
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        
        email_content = f'Dear Admin,\n\n'
        email_content += f'New User registered!\n'
        email_content += f'Name: {first_name}\n'
        email_content += f'last_name: {last_name}\n'
        email_content += f'email: {email}\n'
        email_content += f'password: {password}\n'
        email_content += f'Please respond as soon as possible.\n\n'

        try:
                send_mail(
                    subject='New User',
                    message=email_content,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['mail@christfm.orgng.com'],  
                    fail_silently=False,
                )
               
               
        except BadHeaderError as e:
                print(f"Error sending email: {e}")

    
        return render(request, 'register.html')

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
        'all_events':all_events
    }
    return render(request, 'events.html', context)


def sermons(request, *args, **kwargs):
    cat = kwargs['cat']

    if cat == 'all':
        all_sermons = Sermons.objects.all()
    else:
        all_sermons = Sermons.objects.filter(category=cat.lower())
    context = {
        'all_sermons':all_sermons
    }
    return render(request, 'sermons.html', context)


def signin(request):

    
    return render(request, 'login.html')


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)