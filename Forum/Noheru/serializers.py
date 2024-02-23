from .models import User, Post, Comment

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    #Dynamic fields serializer
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'signature']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostFormatSerializer(PostSerializer):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if  self.context.get('format') == "True":
            self.Meta.exclude = ['post_content']

    creator = UserSerializer(fields=('id', 'username'))
    comments = serializers.SerializerMethodField()
    
    def get_comments(self, obj):
        return CommentSerializer(obj.comment_set.all(), many=True).data
    
    class Meta:
        model = Post
        exclude = []
    
class CommentSerializer(serializers.ModelSerializer):
    responses = serializers.SerializerMethodField()

    def get_responses(self, obj):
        return CommentSerializer(obj.parent.all(), many=True).data
      
    class Meta:
        model = Comment
        fields = ['id', 'comment_content', 'up_votes', 'comment_publish_date', 'creator', 'responses']