# Generated by Django 4.1.7 on 2023-05-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_registration_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='registration_accepted',
            field=models.BooleanField(default=False, help_text="Designates whether this user's registration has been accepted."),
        ),
    ]
