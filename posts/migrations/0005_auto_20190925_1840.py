# Generated by Django 2.2.5 on 2019-09-25 15:40

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190925_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photo',
            field=models.FileField(upload_to=posts.models.user_directory_path),
        ),
    ]