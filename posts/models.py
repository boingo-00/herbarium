from django.db import models
from django.contrib.auth.models import User
import random
import string

# Create your models here.

def buildblock(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

def user_directory_path(post, filename):
    # file will be uploaded to MEDIA_ROOT/<username>/<filename>
    return '{0}/{1}/{2}'.format(User.get_username, buildblock(10), filename)

class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    desc = models.CharField(max_length=3000, verbose_name='Post Description')
    visible = models.BooleanField(default='True', verbose_name='Visible')
    pubdate = models.DateTimeField('Published at:',auto_now=True)
class album(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path)