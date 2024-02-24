from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "Noheru"
urlpatterns = [
    path('user-create/', views.UserC.as_view()),
    path('user-update/<int:pk>/', views.UserU.as_view()),
    path('users/<int:pk>/', views.UserRD.as_view()),
    
    path('post-create/', views.PostC.as_view()),
    path('post-update/<int:pk>/', views.PostU.as_view()),
    path('posts/<int:pk>/', views.PostRD.as_view()),
    path('recent-posts/', views.MostRecentPosts.as_view()),
    
    path('comment-create/', views.CommentC.as_view()),
    path('comment-update/<int:pk>/', views.CommentU.as_view()),
    path('comments/<int:pk>/', views.CommentRD.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)