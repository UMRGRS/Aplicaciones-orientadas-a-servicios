from .models import User, Post, Comment

from rest_framework import serializers

#User serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BasicUserInfoSerializer(UserSerializer):
    class Meta:
        model = User
        exclude = ['password', 'email', 'signature']

#Posts serializers
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostFormatSerializer(PostSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.context.get('format') == "True":
            self.Meta.exclude = ['post_content']

    creator = BasicUserInfoSerializer()

    class Meta:
        model = Post
        exclude = []
        
class UpdatePostSerializer(PostSerializer):
    class Meta:
        model = Post
        exclude = ['post_publish_date', 'up_votes', 'creator']

#Comments serializers
class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class RetrieveCommentsSerializer(CreateCommentSerializer):
    creator = BasicUserInfoSerializer()
    responses = serializers.SerializerMethodField()
    
    def get_responses(self, obj):
        return RetrieveCommentsSerializer(obj.parent.all()[:1], many=True).data
      
    class Meta:
        model = Comment
        exclude=[]  

class UpdateCommentSerializer(CreateCommentSerializer):
    class Meta:
        model = Comment
        exclude=['comment_publish_date', 'creator', 'parent_post', 'parent_comment']