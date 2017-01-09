from django.contrib import admin
from .models import Student
from .models import Teacher
from .models import Subject
from .models import Grade
from .models import TeacherClass

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(TeacherClass)
