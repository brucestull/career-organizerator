# Generated by Django 4.1.7 on 2023-11-18 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("career_organizerator", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The date and time this object was created.",
                        verbose_name="Created",
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time this object was last updated.",
                        verbose_name="Updated",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The name of the skill.",
                        max_length=255,
                        verbose_name="Name",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user who created the skill.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Skills",
            },
        ),
    ]
