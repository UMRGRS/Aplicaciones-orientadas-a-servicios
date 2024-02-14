from rest_framework import serializers
from Serializers_Test.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'password','email','signature']