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
    
    image_files = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    
    video_files = serializers.ListField(
        child=serializers.FileField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Post
        fields = [
            'id', 'user', 'caption', 'content_type', 'text',
            'created_at', 'images', 'videos', 'image_files', 'video_files'
        ]
        read_only_fields = ['user', 'created_at', 'images', 'videos']

    def create(self, validated_data):
        image_files = validated_data.pop('image_files', [])
        video_files = validated_data.pop('video_files', [])

        post = Post.objects.create(**validated_data)

        for image in image_files:
            PostImage.objects.create(post=post, image=image)

        for video in video_files:
            PostVideo.objects.create(post=post, video=video)

        return post
    
      
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # or list specific fields