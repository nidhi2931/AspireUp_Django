from django.db import models
from subjects.models import Subject


class Topic(models.Model):
    subject =models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='subjects')
    name=models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.name

