from .models import User, Post, Comment
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'password', 'email', 'signature']
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'post_title', 'post_summary', 'post_content', 'post_publish_date', 'up_votes', 'creator']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment_content', 'up_votes', 'comment_publish_date', 'creator', 'parent_post', 'parent_comment']