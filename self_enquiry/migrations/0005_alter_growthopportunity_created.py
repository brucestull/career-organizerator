# Generated by Django 4.1.9 on 2023-08-24 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_enquiry', '0004_alter_growthopportunity_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growthopportunity',
            name='created',
            field=models.DateTimeField(help_text='The date and time the growth opportunity was created.'),
        ),
    ]