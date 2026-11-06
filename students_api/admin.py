from django.contrib import admin
from .models import Student

# Register Student so records can also be inspected in Django's admin site.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "course", "email", "created_at")
    search_fields = ("name", "email", "course")
    list_filter = ("course",)
