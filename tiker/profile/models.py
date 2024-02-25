from django.db import models

# Create your models here.
class profilemodel(models.Model):
    name=models.CharField(max_length=100,null=False)
    username=models.CharField(max_length=100,null=False)
    year = models.IntegerField()
    about=models.CharField(max_length=500,null=False)
    photo=models.ImageField(upload_to='photo')
    def __str__(self):
        return self.name