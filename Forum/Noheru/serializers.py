from .models import User, Post, Comment

from rest_framework import serializers

from django.http import HttpResponseBadRequest

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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment_content', 'up_votes', 'comment_publish_date', 'creator']
        
class PostRetrieveSerializer(serializers.ModelSerializer):
    creator = UserSerializer(fields=('id', 'username'))
    comments = CommentSerializer(source='comment_set', many=True)
    
    def to_representation(self, obj):
        ret = super(PostRetrieveSerializer, self).to_representation(obj)
        postFormat = self.context.get('postFormat')
        match postFormat:
            case 'cpr':
                ret.pop('comments')
                ret.pop('post_content')
                return ret 
            case 'com':
                return ret
            case None:
                return ret
            case _:
                ret = {"detail": f'format {postFormat} is invalid'}
                return ret
    class Meta:
        model = Post
        fields = ['id', 'post_title', 'post_summary', 'post_content', 'post_publish_date', 'up_votes', 'creator', 'comments']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_title', 'post_summary', 'post_content', 'creator']