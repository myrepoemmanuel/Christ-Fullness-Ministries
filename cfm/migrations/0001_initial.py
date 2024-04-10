# Generated by Django 4.1.6 on 2024-03-29 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abt_text', models.TextField(max_length=200)),
                ('vision', models.TextField(max_length=2000)),
                ('mission', models.TextField(max_length=2000)),
                ('core_value_1', models.CharField(max_length=200)),
                ('core_value_1_image', models.ImageField(blank=True, null=True, upload_to='core_values_img')),
                ('core_value_2', models.CharField(max_length=200)),
                ('core_value_2_image', models.ImageField(blank=True, null=True, upload_to='core_values_img')),
                ('core_value_3', models.CharField(max_length=200)),
                ('core_value_3_image', models.ImageField(blank=True, null=True, upload_to='core_values_img')),
                ('core_value_4', models.CharField(max_length=200)),
                ('core_value_4_image', models.ImageField(blank=True, null=True, upload_to='core_values_img')),
            ],
            options={
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='GetInvolved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('page_description', models.TextField(max_length=2000)),
                ('page_background', models.ImageField(blank=True, null=True, upload_to='GetInvolved_img')),
                ('department_1', models.CharField(max_length=200)),
                ('department_1_image', models.ImageField(blank=True, null=True, upload_to='GetInvolved_img')),
                ('department_1_description', models.TextField(max_length=200)),
                ('department_2', models.CharField(max_length=200)),
                ('department_2_image', models.ImageField(blank=True, null=True, upload_to='GetInvolved_img')),
                ('department_2_description', models.TextField(max_length=200)),
                ('department_3', models.CharField(max_length=200)),
                ('department_3_image', models.ImageField(blank=True, null=True, upload_to='GetInvolved_img')),
                ('department_3_description', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Get Involved',
            },
        ),
        migrations.CreateModel(
            name='Leaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=20000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='leaders_img')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Leaders',
            },
        ),
    ]
