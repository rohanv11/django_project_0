from django.shortcuts import render

from django.http import HttpResponse

from first_app.models import Students
from datetime import datetime


# Create your views here.
def hello_view(request, name):
    s1 = Students(name=name, city="Mumbai", dob=datetime.now(), age=20)
    s1.save()

    s1 = Students.objects.get(name=name)

    return HttpResponse("Hello, World! " + name + ", age:" + str(s1.age))


