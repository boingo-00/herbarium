from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<username>/post_id_<id>/<filename>
    return '{0}/post_id_{1}/{2}'.format(instance.user.username, instance.post.id, filename)

class post(models.Model):
    user    = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    desc    = models.CharField(max_length=3000, verbose_name='Post Description')
    hidden  = models.BooleanField(verbose_name='Hidden post')
    pubdate = models.DateTimeField('Published at:', auto_now=True)

class album(models.Model):
    user    = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post    = models.ForeignKey(post, default=None, on_delete=models.CASCADE)
    photo   = models.ImageField(upload_to=user_directory_path)