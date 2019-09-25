from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(post, filename):
    # file will be uploaded to MEDIA_ROOT/<username>/<filename>
    return '{0}/{1}'.format(post.userid, filename)

class post(models.Model):
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    desc = models.CharField(max_length=3000, verbose_name='Post Description')
    visible = models.BooleanField(default='True', verbose_name='Visible')
    pubdate = models.DateTimeField('Published at:')

class album(models.Model):
    postid = models.ForeignKey(post, on_delete=models.CASCADE)
    photo = models.FileField(upload_to=user_directory_path)