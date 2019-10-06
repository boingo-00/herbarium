from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import random
import string

# Create your models here.

# def buildblock(size):
#     return ''.join(random.choice(string.ascii_letters) for _ in range(size))

# def userget(instance):
#     return instance.user.id

# def user_directory_path(post, filename):
#     # file will be uploaded to MEDIA_ROOT/<username>/<post>/<filename>
#     return '{0}/{1}'.format(userget, filename)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}/{2}'.format(instance.user.username, instance.post.id, filename)

class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    desc = models.CharField(max_length=3000, verbose_name='Post Description')
    hidden = models.BooleanField(verbose_name='Hidden post')
    pubdate = models.DateTimeField('Published at:',auto_now=True)

class album(models.Model):
    post = models.ForeignKey(post, default=None, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path)