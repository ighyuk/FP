from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    name = models.CharField(max_length=10)
    department = models.CharField(max_length=20)
    student_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.user_id



