# Generated by Django 2.2.5 on 2019-09-27 05:16

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_album_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photo',
            field=models.ImageField(upload_to=posts.models.user_directory_path),
        ),
    ]
