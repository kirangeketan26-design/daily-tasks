"""Project-level URL routing."""
from django.contrib import admin
from django.urls import include, path
from students_api.views import dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("students_api.urls")),  # Delegate /api/ URLs to the app.
    path("", dashboard, name="dashboard"),       # Serve the student dashboard at /.
]
