from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import AddDoc
from .serializers import AddDocsSerializer
from django.db.models import Q
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser,FormParser
from topics.models import *

@api_view(['GET'])
def get_adddocs(request):
    add_docs = AddDoc.objects.filter(Q(files__isnull=False) & Q(topic__isnull=False))
    serializer = AddDocsSerializer(add_docs, many=True)
    print(serializer)
    return Response(serializer.data)

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser])
def create_adddocs(request):
    print("Request Data:", request.data)
    print("Request Files:", request.FILES)
    topic_id = request.data.get('topic')
    print(topic_id)
    if not topic_id:
        return Response({"error":"Topic ID is required."},status=status.HTTP_400_BAD_REQUEST)
    
    try:
        topic=Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        return Response({"error":"Invalid Topic ID"}, status=status.HTTP_400_BAD_REQUEST)
    
    files = request.FILES.getlist('files')
    if not files:
        return Response({"error":"No files provided."},status=status.HTTP_400_BAD_REQUEST)

    uploaded_docs=[]
    for file in files:
        doc_data={"topic":topic.id,"files":file}
        serializer=AddDocsSerializer(data=doc_data)
    
        if serializer.is_valid():
            serializer.save()
            uploaded_docs.append(serializer.data)
        else:
            print("Serializer Errors:", serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response(
        {
            "message": "Files uploaded successfully",
            "uploaded_documents": uploaded_docs,
        },
        status=status.HTTP_201_CREATED
    )