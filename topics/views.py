from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET'])
def get_topics(request):
    topics = Topic.objects.all()
    serializer=TopicsSerializer(topics,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_topics(request):
    serializer = TopicsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


