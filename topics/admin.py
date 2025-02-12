from django.contrib import admin
from .models import *

# Register your models here.

class TopicsAdmin(admin.ModelAdmin):
    list_display=('id','subject_id','subject_name','name')

    def subject_name(self,obj):
        return obj.subject.name

    subject_name.short_description='Subject Name'

admin.site.register(Topic,TopicsAdmin)



