from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class HomepageSliders(models.Model):
    slider_title = models.CharField(max_length=200)
    slider_image = models.ImageField(null=True, blank=True)
    slider_link = models.CharField(max_length=200)
    slider_description = models.TextField(max_length=200)
    
    def __str__(self):
        return self.slider_title
    
    def save(self, *args, **kwargs):
        print(f"this is image url: {self.slider_image.url}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Homepage Sliders'
    
    @property
    def imageURL(self):
        try:
            url = self.slider_image.url
        except:
            url = ''
        return url
    
    
class HomeSections(models.Model):
    # hompage social event boxes
    social_event_1 = models.CharField(null=True, blank=True, max_length=200)
    social_event_1_image = models.ImageField(null=True, blank=True)
    social_event_1_description = models.TextField(null=True, blank=True, max_length=200)

    social_event_2 = models.CharField(null=True, blank=True, max_length=200)
    social_event_2_image = models.ImageField(null=True, blank=True)
    social_event_2_description = models.TextField(null=True, blank=True, max_length=200)

    social_event_3 = models.CharField(null=True, blank=True, max_length=200)
    social_event_3_image = models.ImageField(null=True, blank=True)
    social_event_3_description = models.TextField(null=True, blank=True, max_length=200)

    # hompage aboutus
    about_img = models.ImageField(null=True, blank=True)
    about_description = models.TextField(null=True, blank=True, max_length=200)

    # hompage sermons
    sermon_1_link = models.CharField(null=True, blank=True, max_length=200)
    sermon_2_link = models.CharField(null=True, blank=True, max_length=200)
    sermon_3_link = models.CharField(null=True, blank=True, max_length=200)



    def __str__(self):
        return "Home sections Here"

    class Meta:
        verbose_name_plural = 'Home sections'

    def save(self, *args, **kwargs):
        for sermon in ["sermon_1_link", "sermon_2_link", "sermon_3_link"]:
            field_value = getattr(self, sermon)
            # print(field_value)
            if field_value:
                print(field_value)
                link_code = field_value.split("watch")[1].split("=")[1]
                setattr(self, sermon, link_code)
        super().save(*args, **kwargs)


    @property
    def imageURL1(self):
        try:
            url = self.social_event_1_image.url
        except:
            url = ''
        return url
    
    @property
    def imageURL2(self):
        try:
            url = self.social_event_2_image.url
        except:
            url = ''
        return url
    
    @property
    def imageURL3(self):
        try:
            url = self.social_event_3_image.url
        except:
            url = ''
        return url
    
    
class Leaders(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField(max_length=20000)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Leaders'
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class About(models.Model):
    abt_text = models.TextField(max_length=200)
    vision = models.TextField(max_length=2000)
    mission = models.TextField(max_length=2000)
    core_value_1 = models.CharField(max_length=200)
    core_value_1_image = models.ImageField(null=True, blank=True)

    core_value_2 = models.CharField(max_length=200)
    core_value_2_image = models.ImageField(null=True, blank=True)

    core_value_3 = models.CharField(max_length=200)
    core_value_3_image = models.ImageField(null=True, blank=True)

    core_value_4 = models.CharField(max_length=200)
    core_value_4_image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return "About us"

    class Meta:
        verbose_name_plural = 'About Us'

    @property
    def imageURL1(self):
        try:
            url = self.core_value_1_image.url
        except:
            url = ''
        return url
    
    @property
    def imageURL2(self):
        try:
            url = self.core_value_2_image.url
        except:
            url = ''
        return url
    
    @property
    def imageURL3(self):
        try:
            url = self.core_value_3_image.url
        except:
            url = ''
        return url
    
    @property
    def imageURL4(self):
        try:
            url = self.core_value_4_image.url
        except:
            url = ''
        return url
    

class GetInvolved(models.Model):
    name = models.TextField(max_length=200)
    page_description = models.TextField(max_length=2000)
    page_background = models.ImageField(null=True, blank=True)

    department_1 = models.CharField(max_length=200)
    department_1_image = models.ImageField(null=True, blank=True)
    department_1_description = models.TextField(max_length=200)

    department_2 = models.CharField(max_length=200)
    department_2_image = models.ImageField(null=True, blank=True)
    department_2_description = models.TextField(max_length=200)

    department_3 = models.CharField(max_length=200)
    department_3_image = models.ImageField(null=True, blank=True)
    department_3_description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Get Involved'

    @property
    def pageBackground(self):
        try:
            url = self.page_background.url
        except:
            url = ''
        return url

    @property
    def imageURL1(self):
        try:
            url = self.department_1_image.url
        except:
            url = ''
        return url
    
    @property
    def imageURL2(self):
        try:
            url = self.department_2_image.url
        except:
            url = ''
        return url
    
    @property
    def imageURL3(self):
        try:
            url = self.department_3_image.url
        except:
            url = ''
        return url
    
    
class Events(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=20000)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Events'
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class Sermons(models.Model):
    cats = (
        ('podcast','podcast'),
        ('celebration','celebration'),
        ('discipleship','discipleship'),
        ('children','children')
    )
    category = models.CharField(choices=cats, max_length=200, default="unlabled")
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=20000)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sermons'
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class Gallery(models.Model):
    cats = (
        ('service','service'),
        ('baptism','baptism'),
        ('construction','construction'),
        ('celebration','celebration'),
        ('discipleship','discipleship'),
        ('children','children')
    )
    category = models.CharField(choices=cats, max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Gallery'
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    