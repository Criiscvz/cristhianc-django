# Generated by Django 5.0.6 on 2024-05-13 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='datecompleted',
        ),
        migrations.AddField(
            model_name='task',
            name='datecomplete',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
