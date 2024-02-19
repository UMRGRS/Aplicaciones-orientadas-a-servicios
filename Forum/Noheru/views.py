from rest_framework import status
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer

# Create your views here.

#User endpoints
class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateAPIView):
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_user(pk)
        serializer = UserSerializer(user, fields=('user_name', 'email', 'signature'))
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    queryset = User.objects.all()
    serializer_class = UserSerializer