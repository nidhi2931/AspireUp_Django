from rest_framework import serializers
from .models import Topic
from subjects.models import Subject
from subjects.serializers import *

class TopicsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Topic
        fields=['id','subject','name']
        
