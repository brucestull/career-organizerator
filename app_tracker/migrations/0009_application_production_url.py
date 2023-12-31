# Generated by Django 4.1.9 on 2023-08-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tracker', '0008_application_repository_is_public_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='production_url',
            field=models.URLField(blank=True, help_text="The URL of the application's production deployment.", null=True),
        ),
    ]
