from django.apps import AppConfig

# AppConfig tells Django how this application is registered.
class StudentsApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "students_api"
