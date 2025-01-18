from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tweet, Like, Comment
from .serializers import TweetSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


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
def like_tweet(request):
    if request.method == 'POST':
        data=request.data
        tweet_id=data.get('tweet_id')
        tweet=Tweet.objects.filter(id=tweet_id).first()
        if not tweet:
            return Response({'error':'Tweet not found'}, status=404)
        like, created=Like.objects.get_or_create(tweet=tweet, user=request.user)
        if not created:
            like.delete()
        return Response({'message':'Success'}, status=200)
    return Response({'error':'Invalid request'}, status=400)

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