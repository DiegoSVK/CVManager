from django.contrib import admin
from .models import Resume
# Register your models here.

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title','user','created_at']
    search_fields = ['title','user__username']
    list_filter = ['title','user']

