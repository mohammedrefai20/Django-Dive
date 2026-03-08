from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name="students")
    image = models.ImageField(upload_to='students/', blank=True, null=True)

    def __str__(self):
        return self.name