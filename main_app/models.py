from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Accessory(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('accessory-detail', kwargs={'pk': self.id})

class Jellycat(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    accessories = models.ManyToManyField(Accessory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('jellycat-detail', kwargs={'jellycat_id': self.id})
