# Generated by Django 4.1.9 on 2023-08-27 10:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_tracker', '0017_project_application_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ManyToManyField(help_text='The owner(s) of the project.', related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Owner(s)'),
        ),
    ]
