from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    instructors = models.ForeignKey(
        'instructors.instructor',
        on_delete=models.SET_NULL,
        null=True,
        related_name='courses'
    )
    image = models.ImageField(upload_to='courses/', blank=True, null=True)

    def __str__(self):
        return self.title