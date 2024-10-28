# Generated by Django 5.1.2 on 2024-10-28 07:06

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events1', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='short_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AddField(
            model_name='event',
            name='capacity',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='event',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event_images/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]