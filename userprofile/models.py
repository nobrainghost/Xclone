from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_pics',null=True, blank=True)
    bio = models.TextField(blank=True)
    phoneNumber=models.CharField(max_length=15, blank=True)
    address=models.TextField(blank=True)
    city=models.CharField(max_length=50, blank=True)
    country=models.CharField(max_length=50, blank=True)
    Date_of_birth=models.DateField(null=True, blank=True)
    name=models.CharField(max_length=50, blank=True,null=True)

    def __str__(self):
        return self.user.username