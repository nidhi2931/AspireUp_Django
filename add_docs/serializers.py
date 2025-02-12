from rest_framework import serializers
from .models import AddDoc
from topics.models import *

class AddDocsSerializer(serializers.ModelSerializer):
    topic = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all())
    topic_name=serializers.CharField(source='topic.name')
    subject_name=serializers.CharField(source='topic.subject.name')

    class Meta:
        model = AddDoc
        fields = ['topic','topic_name','subject_name','files']

    def validate(self, data):
        if not data.get('files'):
            raise serializers.ValidationError({"files": "This field is required."})
        return data

