from django.db import models
from topics.models import *

# Create your models here.

class AddDoc(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='topics',default=1)
    files=models.FileField(upload_to='uploads/',blank=True, null=True)

    def __str__(self):
        return f"{self.topic} - {self.files}"
