from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    
class Recipe(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ateria = models.CharField(max_length=200)
    ainekset = models.TextField()
    ohjeet = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
