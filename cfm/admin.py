from django import forms
from django.contrib import admin
from .models import Leaders, About, GetInvolved, HomepageSliders,HomeSections
from .utils import upload_to_cpanel_sftp
import ftplib
# Register your models here.

class HomepageSlidersAdminForm(forms.ModelForm):
    class Meta:
        model = HomepageSliders
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        print(f'this is instance{instance.slider_image.path}')

        if instance.slider_image:
            try:
                # Open and read the image file content in binary mode
                file_path = instance.slider_image.path
                with open(file_path, 'rb') as image_file:
                    image_content = image_file.read()
                ftp_host = 'www.christfm.org'
                ftp_port = 21
                ftp_user = 'christfm@christfm.org'
                ftp_pass = 'aba@christfm24'  # Provide your FTP password here
                remote_file_path = '/home/christf1/christfmMedia'  # Remote path on FTP server

            
                with ftplib.FTP_TLS() as ftp:
                    ftp.connect(ftp_host, ftp_port)
                    ftp.login(ftp_user, ftp_pass)
                    ftp.prot_p()  # Enable data protection
                    ftp.storbinary(f'STOR {remote_file_path}', image_content)
                    print(f"Image uploaded successfully to FTP server at: {remote_file_path}")
            except Exception as e:
                print(f"FTPS Error: {e}")
        if commit:
            instance.save()

        return instance

class HomepageSlidersAdmin(admin.ModelAdmin):
    form = HomepageSlidersAdminForm

admin.site.register(HomepageSliders, HomepageSlidersAdmin)



admin.site.register(HomeSections)
admin.site.register(Leaders)
admin.site.register(About)
admin.site.register(GetInvolved)
