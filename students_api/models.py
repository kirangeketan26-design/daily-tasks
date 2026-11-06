from django.db import models

# A Django model maps this Python class to a table in PostgreSQL.
class Student(models.Model):
    # CharField creates a text/varchar column with a maximum length.
    name = models.CharField(max_length=100)

    # PositiveSmallIntegerField stores a small non-negative integer age.
    age = models.PositiveSmallIntegerField()

    # CharField stores the student's course/program name.
    course = models.CharField(max_length=120)

    # EmailField stores email text and applies basic email validation.
    email = models.EmailField(max_length=254, unique=True)

    # auto_now_add stores the creation timestamp automatically.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Explicit table name makes the generated database table easy to identify.
        db_table = "students_api_student"
        ordering = ["id"]  # Return records in ascending primary-key order.

    def __str__(self):
        # Human-readable label used in Django admin and debugging.
        return f"{self.name} ({self.email})"
