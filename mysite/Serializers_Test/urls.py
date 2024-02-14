from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Serializers_Test import views

app_name = "Serializers_Test"
urlpatterns = [
    path('users/', views.User_list.as_view()),
    path('users/<int:pk>/', views.user_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
