# Generated by Django 4.0.4 on 2022-05-06 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0002_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default=''),
        ),
    ]
