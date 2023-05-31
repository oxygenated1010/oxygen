
from django.urls import path
#from . import views
from .views import Homeview, BlogDetailView, BlogPostView, UpdateBlogPost, DeleteBlogPost, LikeView, AddCommentView



urlpatterns = [
    
    #path('', views.home, name='home'),
    path('', Homeview.as_view(), name='home'),
    path('article-details/<int:pk>', BlogDetailView.as_view(), name='article-details'),
    path('blog_post/', BlogPostView.as_view(), name='blog_post'),
    path('edit_post/<int:pk>', UpdateBlogPost.as_view(), name='edit_post'),
    path('delete_post/<int:pk>', DeleteBlogPost.as_view(), name='delete_post'),
    path('likes/<int:pk>', LikeView, name='like_post'),
    path('article-details/<int:pk>/add_comment', AddCommentView.as_view(), name='add_comment'),
]