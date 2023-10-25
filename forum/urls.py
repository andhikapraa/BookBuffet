from django.urls import path
from forum.views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('post/<int:post_id>', show_post, name='show_post'),
    path('mypost/', show_mypost, name='show_mypost'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-post/', create_post, name='create_post'),
    path('get-post/', get_post, name='get_post'),
    path('get-post/<int:post_id>/', get_post_by_id, name='get_post_by_id'),
    path('get-user/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
    path('get-comments/', get_comment, name='get_comment'),
    path('create-comment/<int:post_id>/', create_comment, name='create_comment'),
    path('get-comment/<int:post_id>/', get_comments_by_id, name='get_comments_by_id'),
    path('delete-comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('delete-post/<int:post_id>/', delete_post, name='delete_post'),
    path('reply/<int:comment_id>/', create_reply, name='create_reply'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)