from . import views
from django.urls import path



urlpatterns = [
    path('', views.home, name = 'home' ),
    path('about/', views.about_us, name = 'about' ),
    path('involve/<slug:slug>', views.solution, name = 'get_involved' ),
    path('signin/', views.signin, name = 'signin' ),
    path('register/', views.register, name = 'register' ),
    path('contact/', views.contactus, name = 'contactus' ),
    path('gallery/<slug:cat>', views.gallery, name = 'gallery' ),
    path('events/', views.events, name = 'events' ),
    path('sermons/<slug:cat>', views.sermons, name = 'sermons' ),
]