from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from Serializers_Test.models import User
from Serializers_Test.serializers import UserSerializer
from rest_framework import generics

# Create your views here.
#Class based views
class User_list(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Function based view
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def user_detail(request, pk, format=None):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        seria = UserSerializer(user)
        return Response(seria.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
