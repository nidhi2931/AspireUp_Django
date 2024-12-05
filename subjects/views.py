from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subject
from .serializers import SubjectSerializer


class AddSubjectView(APIView):
    def post(self,request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class GetSubjectView(APIView):
    def get(self,request):
        subjects=Subject.objects.all()
        serializer=SubjectSerializer(subjects,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
