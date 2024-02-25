from django.db import models
# Create your models here.

class Profile(models.Model):
    profile_name=models.CharField(max_length=200)
    profilephoto=models.FileField(upload_to='docs/profile')
    newspost=models.CharField(max_length=200)
    videopost=models.FileField(upload_to='docs/vedio')
    photopost=models.FileField(upload_to='docs/photo')
    comments=models.CharField(max_length=200)
    likes=models.IntegerField(null=True)
    postdate=models.DateField(null=True,blank=True)

