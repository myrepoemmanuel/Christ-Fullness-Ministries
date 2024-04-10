from django.contrib import admin
from .models import Leaders, About, GetInvolved, HomepageSliders,HomeSections
# Register your models here.

admin.site.register(HomepageSliders)
admin.site.register(HomeSections)
admin.site.register(Leaders)
admin.site.register(About)
admin.site.register(GetInvolved)
