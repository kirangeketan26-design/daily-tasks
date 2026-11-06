from rest_framework.test import APITestCase
from rest_framework import status
from .models import Student

# APITestCase provides an API test client and an isolated test database.
class StudentCRUDTests(APITestCase):
    def setUp(self):
        # Create one known record before each test.
        self.student = Student.objects.create(
            name="Test Student",
            age=20,
            course="Computer Engineering",
            email="test.student@example.com",
        )
        self.list_url = "/api/students/"

    def test_get_student_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_post_create_student(self):
        payload = {
            "name": "New Student",
            "age": 21,
            "course": "IT",
            "email": "new.student@example.com",
        }
        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Student.objects.filter(email=payload["email"]).exists())

    def test_patch_student(self):
        response = self.client.patch(
            f"{self.list_url}{self.student.pk}/",
            {"course": "Cloud Computing"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.course, "Cloud Computing")

    def test_delete_student(self):
        response = self.client.delete(f"{self.list_url}{self.student.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())
