from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.utils import timezone
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from .forms import StudentForm, TeacherForm, GradeForm, SearchForm
from .models import Student, Teacher, Grade

# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request,"school/home.html")

#############################student
def student_list(request):
    students = Student.objects.order_by('lastname')
    return render(request, 'school/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'school/student_detail.html', {'student': student})

def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.created = timezone.now()
            student.modified = timezone.now()
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'school/student_edit.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            # post.author = request.user
            student.modified = timezone.now()
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'school/student_edit.html', {'form': form})
##########################################################
#############################teacher
def teacher_list(request):
    teachers = Teacher.objects.order_by('lastname')
    return render(request, 'school/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'school/teacher_detail.html', {'teacher': teacher})

def teacher_new(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.created = timezone.now()
            teacher.modified = timezone.now()
            teacher.save()
            return redirect('teacher_detail', pk=teacher.pk)
    else:
        form = TeacherForm()
    return render(request, 'school/teacher_edit.html', {'form': form})

def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            teacher = form.save(commit=False)
            # post.author = request.user
            teacher.modified = timezone.now()
            teacher.save()
            return redirect('teacher_detail', pk=teacher.pk)
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'school/teacher_edit.html', {'form': form})
##########################################################
#############################grade
def grade_list(request):
	# grades = Grade.objects.filter(subject="Maths")
	grades = Grade.objects.order_by('student')
	return render(request, 'school/grade_list.html', {'grades': grades})

def grade_detail(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    return render(request, 'school/grade_detail.html', {'grade': grade})

def grade_new(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.total50 = total_50(
            	form.cleaned_data['classtest1'], 
            	form.cleaned_data['classtest2'], 
            	form.cleaned_data['groupwork'], 
            	form.cleaned_data['projectwork']
            	)
            grade.exams50 = float(form.cleaned_data['examsscore']) * 0.5
            grade.total100 = grade.total50 + grade.exams50
            grade.created = timezone.now()
            grade.save()
            return redirect('grade_detail', pk=grade.pk)
    else:
        form = GradeForm()
    return render(request, 'school/grade_new.html', {'form': form})


def total_50(test1, test2, group, project):
	sum = float(test1 + test2 + group + project)
	return(sum * 0.5)

def grade_filter(request):
    if request.method == "GET":
        subject = request.GET.get('subject','')
        sclass = request.GET.get('sclass','')
        grades = Grade.objects.filter(subject=subject, sclass=sclass)
        return render(request, 'school/grade_list.html', {'grades':grades})
        # message = "You searched for: %s" % request.GET.get('subject','asdasdasdas')
        # message = "You searched for: %s" % request.GET.get('subject','asdasdasdas')
        # return HttpResponse(results)
		# form = SearchForm(request.POST)
		# if form.is_valid():
		# 	subject = form.cleaned_data['subject']
		# 	return render(request, 'school/grade_list.html', {'form': form, 'grades': grades})
	   # return render(request, 'school/grade_list.html', {'grades': grades})

		# 		# sclass = request.GET.get('sclass', '')
		# 	sgrades = Grade.objects.all()
		# 	return render(request, 'school/grade_list.html', {'sgrades': sgrades})
	# if request.method == "POST":
	# 	form = ClassSubjectSearchForm(request.POST)
	# 	if form.is_valid():
	# 		grades1 = Grade.objects.filter(subject="Maths")
	# # 		grades = Grade.objects.get(subject="Maths")
	# 		return render(request, 'school/grade_list.html', {'grades1': grades1})


# def contact(request):
#     form_class = ContactForm
    
#     return render(request, 'contact.html', {
#         'form': form_class,
#     })
