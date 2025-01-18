from django.shortcuts import render

# Create your views here.
#Authentication
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from datetime import timezone,timedelta

@api_view(['POST'])
def register_user(request):
    try:
        data=request.data
        username=data['username']
        email=data['email']
        password=make_password(data['password'])
        user=User(username=username,email=email,password=password)
        user.save()
        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected(request):
    return Response(status=status.HTTP_200_OK)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response=super().post(request, *args, **kwargs)

        access_token=response.data['access']
        refresh_token=response.data['refresh']

        expires=timedelta(days=1)
        response.set_cookie(
            'access_token',
            access_token,
            expires=expires,
            httponly=True,
            secure=True,
            samesite='Lax')
        response.set_cookie(
            'refresh_token',
            refresh_token,
            expires=expires,
            httponly=True,
            secure=True,
            samesite='Lax')
        return response

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token=request.COOKIES.get('refresh_token')
        if refresh_token is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        response=super().post(request, *args, **kwargs)
        new_access=response.data['access']
        expires=timedelta(days=1)
        response.set_cookie(
            'access_token',
            new_access,
            expires=expires,
            httponly=True,
            secure=True,
            samesite='Lax')
        return response

@api_view(['POST'])
def logout(request):
    response=Response({'message':'Logged out'},status=status.HTTP_200_OK)
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response