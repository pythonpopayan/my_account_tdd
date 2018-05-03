from django.db import models
from django.contrib.auth.models import User


class owner(models.Model):
    """implements UserProfile model"""
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_img', default='no-user.svg')
    notes = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
