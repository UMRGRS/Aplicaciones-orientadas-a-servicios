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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment_content', 'up_votes', 'comment_publish_date', 'creator']
        
class PostSerializer(serializers.ModelSerializer):
    creator = UserSerializer(fields=('id', 'username'))
    comments = CommentSerializer(source='comment_set', many=True)
    
    def to_representation(self, obj):
        ret = super(PostSerializer, self).to_representation(obj)
        postFormat = self.context.get('postFormat')
        if postFormat == 'compressed':
            ret.pop('post_content')
        else:
            return ret 
        return ret
    
    class Meta:
        model = Post
        fields = ['id', 'post_title', 'post_summary', 'post_content', 'post_publish_date', 'up_votes', 'creator', 'comments']