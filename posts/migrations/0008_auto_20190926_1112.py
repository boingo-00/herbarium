# Generated by Django 2.2.5 on 2019-09-26 08:12

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_album_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.FileField(null=True, upload_to=posts.models.user_directory_path),
        ),
        migrations.DeleteModel(
            name='album',
        ),
    ]
