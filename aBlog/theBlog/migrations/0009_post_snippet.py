# Generated by Django 4.0.4 on 2022-05-13 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0008_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read blog post..', max_length=255),
        ),
    ]
