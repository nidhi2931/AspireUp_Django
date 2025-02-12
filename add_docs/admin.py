from django.contrib import admin
from .models import AddDoc  # Import your model

@admin.register(AddDoc)
class AddDocsAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'files')  # Fields to display in the admin panel


