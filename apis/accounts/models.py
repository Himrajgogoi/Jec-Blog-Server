from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete= models.CASCADE, null = True, related_name='userprofile')
    bio = models.TextField(blank=True, null=True)
    dp = models.ImageField(upload_to = "dps/", blank= True, null = True)

    def ___str__(self):
        return str(self.user)