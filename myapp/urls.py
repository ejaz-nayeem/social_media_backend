from django.urls import path
from .views import post_list_create, comment_list_create, delete_post, update_post,get_all_posts,get_single_post, get_user_posts

urlpatterns = [
    path('posts/create/', post_list_create, name='post-list-create'),
    path('posts/get_all_posts/', get_all_posts, name='get_all_posts'),
    path('posts/user/<int:user_id>/', get_user_posts, name='get_user_posts'),

    path('posts/<int:pk>/', get_single_post, name='get_single_post'),
    path('posts/<int:pk>/delete/', delete_post, name='delete_post'),
    path('posts/<int:pk>/update/', update_post),
    path('comments/', comment_list_create, name='comment-list-create')
]
