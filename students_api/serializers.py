from rest_framework import serializers
from .models import Student

# ModelSerializer builds serializer fields from the Student model.
# It converts database model objects to JSON and validates incoming API data.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # These are the fields exposed through the REST API.
        fields = ["id", "name", "age", "course", "email", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_age(self, value):
        # Field-level validation: reject ages outside a reasonable student range.
        if value < 1 or value > 100:
            raise serializers.ValidationError("Age must be between 1 and 100.")
        return value

    def validate_name(self, value):
        # Normalize whitespace so names are stored consistently.
        cleaned = value.strip()
        if not cleaned:
            raise serializers.ValidationError("Name cannot be empty.")
        return cleaned
