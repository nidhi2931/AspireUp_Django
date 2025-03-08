from rest_framework import serializers
from .models import Topic
from subjects.models import Subject
from subjects.serializers import *


class TopicsSerializer(serializers.ModelSerializer):
    subject_name = serializers.SerializerMethodField()  # Add subject_name field

    class Meta:
        model = Topic
        fields = ['id', 'name', 'subject_name']  # Include subject_name instead of subject

    def get_subject_name(self, obj):
        return obj.subject.name if obj.subject else None