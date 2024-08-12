from django.contrib import admin
from .models import Leaders, About, GetInvolved, HomepageSliders,HomeSections


import environ
env = environ.Env()
environ.Env.read_env()
# Register your models here.

admin.site.register(HomepageSliders)
admin.site.register(HomeSections)
admin.site.register(Leaders)
admin.site.register(About)
admin.site.register(GetInvolved)
