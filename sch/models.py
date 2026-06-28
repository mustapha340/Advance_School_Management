from django.db import models

# 1. Table ya Madarasa
class ClassRoom(models.Model):
    name = models.CharField(max_length=50, unique=True)
    section = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.section if self.section else ''}"

# 2. Table ya Wanafunzi
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=50, unique=True)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.reg_number})"