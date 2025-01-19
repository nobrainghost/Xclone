from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Follow(models.Model):
    follower=models.ForeignKey(User,related_name='following',on_delete=models.CASCADE)
    followed=models.ForeignKey(User,related_name='followed',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=['follower','followed']

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"
    