from rest_framework import serializers
from .models import Follow
from django.contrib.auth.model import User

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Follow
        fields=['follower','followed','created_at']
        