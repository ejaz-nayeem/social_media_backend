from rest_framework import serializers
from .models import Post, Comment, PostImage, PostVideo

# serializers.py


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']

class PostVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVideo
        fields = ['id', 'video']

class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    videos = PostVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'caption', 'content_type', 'text', 'created_at', 'images', 'videos']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # or list specific fields