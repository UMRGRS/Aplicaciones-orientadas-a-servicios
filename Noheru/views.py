from rest_framework import status
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Post, Comment
from .serializers import UserSerializer, PostFormatSerializer, PostSerializer, UpdatePostSerializer, CreateCommentSerializer, RetrieveCommentsSerializer, UpdateCommentSerializer

#User endpoints
#create users -
class UserC(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Update user info -
class UserU(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Retrieve and delete users -
class UserRD(generics.DestroyAPIView):
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    queryset = User.objects.all()
    serializer_class = UserSerializer   

#Post endpoints
#create posts -
class PostC(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#update posts -
class PostU(generics.UpdateAPIView):
    queryset= Post.objects.all()
    serializer_class = UpdatePostSerializer

#Retrieve and delete posts -
class PostRD(generics.DestroyAPIView):
    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        postFormat= request.GET.get('compressed')
        if postFormat == "True" or postFormat == "False": 
            post = self.get_post(pk)
            serializer = PostFormatSerializer(post, context={'format':postFormat})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'details':'compressed argument must be either True or False'}, status=status.HTTP_400_BAD_REQUEST)

    queryset = Post.objects.all()
    serializer_class = PostFormatSerializer

#Retrieve the most recent posts -
class MostRecentPosts(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all().order_by('-post_publish_date')[:5]
        serializer = PostFormatSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Comments end points
#Create comments -
class CommentC(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer

#Update comment info
class CommentU(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = UpdateCommentSerializer

#Retrieve and delete comments -
class CommentRD(generics.DestroyAPIView):
    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        comments = post.comment_set.all()[:20]
        serializer = RetrieveCommentsSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer


    