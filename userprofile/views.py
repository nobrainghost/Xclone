from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    serializer = UserProfileSerializer(user_profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)