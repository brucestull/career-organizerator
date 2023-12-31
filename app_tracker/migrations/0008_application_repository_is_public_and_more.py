# Generated by Django 4.1.9 on 2023-08-12 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tracker', '0007_application_has_email_sending_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='repository_is_public',
            field=models.BooleanField(default=False, help_text="Whether or not the application's repository is public."),
        ),
        migrations.AlterField(
            model_name='application',
            name='has_email_sending',
            field=models.BooleanField(default=False, help_text='Whether or not the application has email sending capabilities.'),
        ),
    ]
