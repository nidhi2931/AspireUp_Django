from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import AddDoc
from .serializers import AddDocsSerializer
from django.db.models import Q
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser,FormParser


@api_view(['GET'])
def get_adddocs(request):
    add_docs = AddDoc.objects.filter(Q(files__isnull=False) & Q(topic__isnull=False))
    serializer = AddDocsSerializer(add_docs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser])
def create_adddocs(request):
    print("Request Data:", request.data)
    print("Request Files:", request.FILES)
    serializer = AddDocsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,
            {"message": "Files uploaded successfully"},
            status=status.HTTP_201_CREATED
        )
    print("Serializer Errors:", serializer.errors)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
