from django.db import models

class instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='instructors/', blank=True, null=True)

    def __str__(self):
        return self.name