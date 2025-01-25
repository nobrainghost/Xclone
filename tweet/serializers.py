from rest_framework import serializers
from .models import Tweet, Like
import humanize
from datetime import datetime

class TweetSerializer(serializers.ModelSerializer):
    created_at_human=serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = ['id', 'content', 'media', 'created_at_human', 'user']
    
    def get_created_at_human(self, obj):
        return humanize.naturaltime(obj.created_at)
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'