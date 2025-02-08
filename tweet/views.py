from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tweet, Like, Comment
from .serializers import TweetSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import humanize
from datetime import datetime

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_tweet(request):
    if request.method == 'POST':
        data=request.data
        content=data.get('content')
        media=data.get('media')

        if not content:
            return Response({'error':'Content is required'}, status=400)
        tweet=Tweet.objects.create(content=content, user=request.user)
        if media:
            tweet.media=media
            tweet.save()
        serializer=TweetSerializer(tweet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'error':'Invalid request'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_tweet(request,tweet_id):
    tweet=Tweet.objects.filter(id=tweet_id).first()
    if not tweet:
        return Response({"detail":"Tweet not found"},status=status.HTTP_404_NOT_FOUND)
    
    if tweet.user != request.user:
        return Response({"Detail":"Cannot Delete Other User's Tweet"})
    
    tweet.delete()
    return Response({"Message":"Tweet Deleted Succesfully"})

@csrf_exempt
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def like_tweet(request,tweet_id):
    
    tweet=Tweet.objects.filter(id=tweet_id).first()
    if not tweet:
        return Response({'error':'Tweet not found'}, status=404)
    if request.method == 'POST':
        like, created = Like.objects.get_or_create(user=request.user, tweet=tweet)
        if not created:
            return Response({"detail": "You have already liked this tweet."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Tweet liked."}, status=status.HTTP_201_CREATED)
    if request.method=='DELETE':
        like=Like.objects.filter(user=request.user,tweet=tweet).first()
        if not like:
            return Response({"Error":"Tweet not Liked"},status=status.HTTP_400_BAD_REQUEST) 
        like.delete()
    return Response({'Success':'Like Removed'}, status=status.HTTP_200_OK)


# def unlike_tweet(request):
#     if request.method=='POST':
#         data=request.data
#         tweet_id=data.get('tweet_id')
#         tweet=Tweet.objects.filter(id=tweet_id).first()
#         if not tweet:
#             return Response({'error':'Tweet not found'}, status=404)
#         unlike,created=Like.objects.delete(tweet=tweet,user=request.user)
#         if not created:
#             unlike.delete()
#         return Response({'Message':'Success'}, status=404)
#     return Response({'error':'Invalid REquest'}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_tweet(request):
    pass
class TweetPagination(PageNumberPagination):
    page_size=10

@api_view(['POST','GET'])
def time_line(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    paginator=TweetPagination()
    result_page=paginator.paginate_queryset(tweets,request)
    serializer=TweetSerializer(result_page,many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def users_tweets(request,username):
    user=User.objects.get(username=username)
    #convert linux time to human readable time


    if not user:
        return Response({"Detail":"No user with such details was found"})
    tweets=Tweet.objects.filter(user=user).order_by('-created_at')
    
    
    serializer=TweetSerializer(tweets,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_tweet(request):
    if request.method == 'POST':
        data=request.data
        tweet_id=data.get('tweet_id')
        content=data.get('content')
        tweet=Tweet.objects.filter(id=tweet_id).first()
        if not tweet:
            return Response({'error':'Tweet not found'}, status=404)
        if not content:
            return Response({'error':'Content is required'}, status=400)
        comment=Comment.objects.create(tweet=tweet, user=request.user, content=content)
        return Response({'message':'Success'}, status=200)
    return Response({'error':'Invalid request'}, status=400)

##RETWEETS