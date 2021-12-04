from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ExtraData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, null=True)
    proj = models.BigIntegerField(null=True)  
    
    def __str__(self):
        return f'{self.user.username} ExtraData' 