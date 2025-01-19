from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    content=models.TextField()
    media=models.FileField(upload_to='Tweetmedia/', blank=True, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at=models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Tweet at {self.created_at}"
    
class Like(models.Model):
    tweet=models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('tweet', 'user')

    def __str__(self):
        return f"{self.user.username} Like {self.tweet.id}"
    


class Comment(models.Model):
    tweet=models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Comment on {self.tweet.id}"