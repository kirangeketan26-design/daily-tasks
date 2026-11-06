from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Student
from .serializers import StudentSerializer

# The dashboard view serves the HTML interface. CRUD data still travels via API.
def dashboard(request):
    return render(request, "students_api/dashboard.html")


# ListCreateAPIView automatically implements:
# GET  /api/students/  -> list all Student rows
# POST /api/students/  -> validate and create a Student row
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()  # Django ORM query for PostgreSQL records.
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]   # Suitable for this local classroom practical.


# RetrieveUpdateDestroyAPIView automatically implements:
# GET    /api/students/<id>/ -> retrieve one row
# PUT    /api/students/<id>/ -> update all editable fields
# PATCH  /api/students/<id>/ -> update only supplied fields
# DELETE /api/students/<id>/ -> delete the row
class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
