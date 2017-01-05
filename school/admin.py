from django.contrib import admin
from .models import Student
from .models import Teacher
from .models import Grade

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Grade)
