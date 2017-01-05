from __future__ import unicode_literals
from django.utils import timezone

from django.db import models


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class Student(models.Model):
    # author = models.ForeignKey('auth.User')
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=10)
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES,default='Male',)
    residence = models.TextField()
    address = models.TextField()
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s %s" % (self.firstname, self.middlename, self.lastname)


class Teacher(models.Model):
    # author = models.ForeignKey('auth.User')
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=10)
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES,default='Male',)
    residence = models.TextField()
    address = models.TextField()
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s %s" % (self.firstname, self.middlename, self.lastname)

class Grade(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject = models.CharField(max_length=50)
	classtest1 = models.DecimalField(max_digits=5, decimal_places=2)
	classtest2 = models.DecimalField(max_digits=5, decimal_places=2)
	groupwork = models.DecimalField(max_digits=5, decimal_places=2)
	projectwork = models.DecimalField(max_digits=5, decimal_places=2)
	total50 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	examsscore = models.DecimalField(max_digits=5, decimal_places=2)
	exams50 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	total100 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "%s %s" % (self.student, self.subject)