from django.db import models
from student.models import Student

class Result(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    subject1 = models.CharField(max_length=100)
    marks1 = models.PositiveIntegerField()

    subject2 = models.CharField(max_length=100)
    marks2 = models.PositiveIntegerField()

    subject3 = models.CharField(max_length=100)
    marks3 = models.PositiveIntegerField()

    subject4 = models.CharField(max_length=100)
    marks4 = models.PositiveIntegerField()

    subject5 = models.CharField(max_length=100)
    marks5 = models.PositiveIntegerField()

    def total_marks(self):
        return self.marks1 + self.marks2 + self.marks3 + self.marks4 + self.marks5

    def percentage(self):
        return self.total_marks() / 5

    def __str__(self):
        return f"{self.student.full_name} Result"