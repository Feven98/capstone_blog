# Generated by Django 4.1.6 on 2023-02-05 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='spoiler',
            field=models.CharField(default='Click Link To Read More...', max_length=150),
        ),
    ]