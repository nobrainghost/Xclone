from .models import UserProfile
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'phoneNumber', 'address', 'city', 'country', 'Date_of_birth']
