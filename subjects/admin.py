from django.contrib import admin
from .models import Subject
# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=('id','name')
    search_fields=('name',)


