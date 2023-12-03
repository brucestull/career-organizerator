# Generated by Django 4.1.7 on 2023-11-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cbt", "0006_rename_cognativedistortion_cognitivedistortion"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="thought",
            name="cognative_distortion",
        ),
        migrations.AddField(
            model_name="thought",
            name="cognitive_distortion",
            field=models.ManyToManyField(
                help_text="The cognitive distortion of the thought.",
                related_name="thoughts",
                to="cbt.cognitivedistortion",
            ),
        ),
        migrations.AlterField(
            model_name="cognitivedistortion",
            name="description",
            field=models.TextField(
                help_text="The description of the cognitive distortion.",
                verbose_name="Description",
            ),
        ),
        migrations.AlterField(
            model_name="cognitivedistortion",
            name="name",
            field=models.CharField(
                help_text="The name of the cognitive distortion.",
                max_length=150,
                verbose_name="Cognative Distortion",
            ),
        ),
    ]