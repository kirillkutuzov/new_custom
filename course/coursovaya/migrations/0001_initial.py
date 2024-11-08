# Generated by Django 5.1.2 on 2024-10-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='twoFactorAuthentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/images')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_authentication', models.BooleanField(default=False)),
            ],
        ),
    ]
