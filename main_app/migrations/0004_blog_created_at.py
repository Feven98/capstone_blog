# Generated by Django 4.1.5 on 2023-02-01 21:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_blog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
