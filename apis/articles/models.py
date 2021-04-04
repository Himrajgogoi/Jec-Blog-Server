from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    username = models.CharField(max_length=20, blank = False)
    textArea = models.TextField(blank=False)
    header = models.TextField(blank=False)
    image   =models.ImageField(upload_to = "articles/", null=True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "articles", null=True)
    createdAt = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.textArea
        