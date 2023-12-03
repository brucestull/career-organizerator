# Generated by Django 4.1.7 on 2023-08-08 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cbt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time this object was created.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='The date and time this object was last updated.', verbose_name='Updated')),
                ('name', models.CharField(help_text='A summary of the thought.', max_length=250, verbose_name='Summary')),
                ('description', models.TextField(help_text='The description of the thought.', verbose_name='Description')),
                ('user', models.ForeignKey(help_text='The user that has the thought.', on_delete=django.db.models.deletion.CASCADE, related_name='thoughts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Thought',
                'verbose_name_plural': 'Thoughts',
                'ordering': ['name'],
            },
        ),
    ]
