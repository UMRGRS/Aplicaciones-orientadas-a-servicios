from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "Noheru"
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
    path('posts/', views.PostsList.as_view()),
    path('posts/<int:pk>/', views.PostsDetails.as_view()),
    path('comments/', views.CommentsList.as_view()),
    path('comments/<int:pk>/', views.CommentsDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)