# Generated by Django 4.1.7 on 2023-09-24 20:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_tracker", "0030_application_is_adapted_repository"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="reference_url",
            field=models.URLField(
                blank=True,
                help_text="The URL of the application's reference.",
                null=True,
                verbose_name="Reference URL",
            ),
        ),
    ]
