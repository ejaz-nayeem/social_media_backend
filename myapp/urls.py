from django.urls import path
from .views import post_list_create, comment_list_create, delete_post, update_post

urlpatterns = [
    path('posts/', post_list_create, name='post-list-create'),
    path('posts/<int:pk>/delete/', delete_post, name='delete_post'),
    path('posts/<int:pk>/update/', update_post),
    path('comments/', comment_list_create, name='comment-list-create')
]
