from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "Noheru"
urlpatterns = [
    path('user-create/', views.CreateUser.as_view()),
    path('user/<int:pk>/', views.UserDetails.as_view()),
    path('post-create/', views.CreatePost.as_view()),
    path('post/<int:pk>/<str:postFormat>/', views.PostDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)