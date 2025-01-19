from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Follow
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_a_user(request,username):
    try:
        to_follow=User.objects.get(username=username)
        follower=request.user
        if follower==to_follow:
            return Response({"Error":"Can not Follow Yourself"},status=status.HTTP_400_BAD_REQUEST)
        
        if Follow.objects.filter(follower=follower,followed=to_follow).exists():
            return Response({"Error":"Already Following"})
        
        Follow.objects.create(follower=follower,followed=to_follow)
        return Response({"Message":"Followed"},status=status.HTTP_201_CREATED)
    
    except User.DoesNotExist:
        return Response({"Error":"User Not Found"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def unfollow_someone(request,username):
    try:
        to_unfollow=User.objects.get(username=username)
        follower=request.user

        follow=Follow.objects.filter(follower=follower,followed=to_unfollow).first()
        if not follow:
            return Response({"Error":"Not Following this User"},status=status.HTTP_400_BAD_REQUEST)
        
        follow.delete()
        return Response({"Message":"Unfollowed"})
    
    except User.DoesNotExist:
        return Response({"Error":"User not Found"})
    

@api_view(['GET'])
def fetch_followers(request,username):
    try:
        user=User.objects.get(username=username)
        followers=Follow.objects.filter(followed=user)
        follower_usernames=[follow.follower.username for follow in followers]
        return Response({"Followers":follower_usernames},status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"Error":"User Not Found"},status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def fetch_following(request,username):
    try:
        user=User.objects.get(username=username)
        following=user.following.all()
        following_usernames=[followed.username for followed in following]
        return Response(following_usernames)
    except User.DoesNotExist:
        return Response({"Error":"User Does Not Exist"},status=status.HTTP_400_BAD_REQUEST)
        

        
