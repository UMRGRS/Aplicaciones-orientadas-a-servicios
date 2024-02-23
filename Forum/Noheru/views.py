from rest_framework import status
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Post, Comment
from .serializers import UserSerializer, PostRetrieveSerializer, PostSerializer, CommentSerializer

#User endpoints
#create new users
class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Retrieve, update and delete users
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_user(pk)
        serializer = UserSerializer(user, fields=('id', 'username', 'email', 'signature'))
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    queryset = User.objects.all()
    serializer_class = UserSerializer   

#Post endpoints
#create new posts
class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#update posts
class UpdatePost(generics.UpdateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer

#Retrieve and delete posts
class PostDetails(generics.DestroyAPIView):
    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, postFormat, format=None):
        post = self.get_post(pk)
        serializer = PostRetrieveSerializer(post, context={'postFormat':postFormat})
        return Response(serializer.data, status=status.HTTP_200_OK)

    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer
    
class MostRecentPosts(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all().order_by('-post_publish_date')[:5]
        serializer = PostRetrieveSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)