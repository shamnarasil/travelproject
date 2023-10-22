from django.db import models
# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
class Team(models.Model):
    image=models.ImageField(upload_to='images')
    name = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
         return self.name