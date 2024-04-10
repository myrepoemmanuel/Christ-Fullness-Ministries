from . import views
from django.urls import path



urlpatterns = [
    path('', views.home, name = 'home' ),
    path('about/', views.about_us, name = 'about' ),
    path('involve/<slug:slug>', views.solution, name = 'get_involved' ),
    path('signin/', views.signin, name = 'signin' ),
    path('register/', views.register, name = 'register' ),
]