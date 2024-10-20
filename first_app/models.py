from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(null=True)
    age = models.IntegerField(null=True)

class Courses(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Enrollments(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)



class TestTable(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = "my_table"
        ordering = ["name"]
