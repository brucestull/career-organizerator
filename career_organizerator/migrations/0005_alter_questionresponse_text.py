# Generated by Django 4.1.7 on 2023-11-18 22:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("career_organizerator", "0004_questionresponse"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionresponse",
            name="text",
            field=models.TextField(
                help_text="The text of the question response.", verbose_name="Text"
            ),
        ),
    ]
