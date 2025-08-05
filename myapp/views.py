from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment, PostImage, PostVideo
from .serializers import PostSerializer, CommentSerializer

@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def post_list_create(request):
    
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass
        
@api_view(['GET'])

def get_all_posts(request):
    try:
        
        if request.method == 'GET':
            
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

@api_view(['GET'])
def get_user_posts(request, user_id):
    posts = Post.objects.filter(user_id=user_id)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_post(request, pk):
    try:
        if request.method == 'GET':
            
            posts = Post.objects.get(pk=pk)
            serializer = PostSerializer(posts)
            return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

    

    if post.user != request.user:
        return Response({'error': 'You are not allowed to see this post'}, status=403)

    

@api_view(['GET', 'POST'])
def comment_list_create(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

    print("Logged-in user:", request.user)
    print("Post owner:", post.user)

    if post.user != request.user:
        return Response({'error': 'You are not allowed to delete this post'}, status=403)

    post.delete()
    return Response({'message': 'Post deleted successfully'}, status=204)


@api_view(['PUT'])

def update_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

    # Ownership check
    if post.user != request.user:
        return Response({'error': 'You are not allowed to edit this post'}, status=403)

    # Partial update allowed (can update some fields)
    serializer = PostSerializer(post, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
