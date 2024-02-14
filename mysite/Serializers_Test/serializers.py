from rest_framework import serializers
from Serializers_Test.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_name = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=254)
    signature = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.signature = validated_data.get('signature', instance.signature)
        return instance