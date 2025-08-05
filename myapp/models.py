from django.db import models
from cloudinary.models import CloudinaryField

class library(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = CloudinaryField('image')
    video = CloudinaryField('video')



from django.contrib.auth.models import User

# User Profile (optional)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

# Post model
# models.py

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    caption = models.CharField(max_length=255, blank=True)
    content_type = models.CharField(max_length=10, choices=[
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
    ])
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')

class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='videos')
    video = CloudinaryField('video')
    
    def __str__(self):
        return f"Video for post {self.post.id}"


# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.post.id}"
           