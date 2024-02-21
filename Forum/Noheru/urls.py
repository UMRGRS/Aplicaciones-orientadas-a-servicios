from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "Noheru"
urlpatterns = [
    path('users/', views.CreateUser.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
    path('comments/<int:pk>/', views.Comments.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)