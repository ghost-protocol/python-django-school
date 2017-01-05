from django import forms
from .models import Student
from .models import Teacher
from .models import Grade

from django.core.urlresolvers import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset

class StudentForm(forms.ModelForm):
        
    class Meta:
        model = Student
        fields = [
            'firstname',
            'middlename',
            'lastname',
            'dateofbirth',
            'gender',
            'residence',
            'address',
            'contact',
            'email'
        ]

    def __init__(self, *args, **kwargs):
       super(StudentForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_id = 'id-student-form'
       self.helper.form_method = 'post'
       self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
       self.helper.form_class = 'form-horizontal'
       self.helper.layout = Layout(
           Fieldset('Personal',
                    # Field('firstname', placeholder='first name', css_class="some-class"),
                    Field('firstname', css_class="some-class"),
                    Field('middlename', css_class="some-class"),
                    Field('lastname', css_class="some-class"),
                    Field('dateofbirth', placeholder='yyyy-mm-dd', css_class="some-class"),
                    Field('gender', css_class="some-class"),),
           Fieldset('Contact', 'email', 'contact'),)
           # Fieldset('Contact data', 'email', 'contact', style="color: brown;"),)

       # self.helper = FormHelper()
       # self.helper.form_id = 'id-student-form'
       # self.helper.form_method = 'post'
       # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))

class TeacherForm(forms.ModelForm):
        
    class Meta:
        model = Teacher
        fields = [
            'firstname',
            'middlename',
            'lastname',
            'dateofbirth',
            'gender',
            'residence',
            'address',
            'contact',
            'email'
        ]

    def __init__(self, *args, **kwargs):
       super(TeacherForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_id = 'id-teacher-form'
       self.helper.form_method = 'post'
       self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
       self.helper.form_class = 'form-horizontal'
       self.helper.layout = Layout(
           Fieldset('Personal',
                    # Field('firstname', placeholder='first name', css_class="some-class"),
                    Field('firstname', css_class="some-class"),
                    Field('middlename', css_class="some-class"),
                    Field('lastname', css_class="some-class"),
                    Field('dateofbirth', placeholder='yyyy-mm-dd', css_class="some-class"),
                    Field('gender', css_class="some-class"),),
           Fieldset('Contact', 'email', 'contact'),)

########################################################
#######################grade form

class GradeForm(forms.ModelForm):
        
    class Meta:
        model = Grade
        fields = [
            'student',
            'subject',
            'classtest1',
            'classtest2',
            'groupwork',
            'projectwork',
            'examsscore',
        ]

    def __init__(self, *args, **kwargs):
       super(GradeForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_id = 'id-grade-form'
       self.helper.form_method = 'post'
       self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
       self.helper.form_class = 'form-horizontal'
       # self.helper.layout = Layout(
       #     Fieldset(
       #              Field('student', css_class="some-class"),
       #              # Field('subject', css_class="some-class"),
       #              # Field('classtest1', css_class="some-class"),
       #              # Field('classtest2', css_class="some-class"),
       #              # Field('groupwork', css_class="some-class"),
       #              # Field('projectwork', css_class="some-class"),
       #              # Field('total50', css_class="some-class"),
       #              # Field('examsscore', css_class="some-class"),
       #              # Field('total100', css_class="some-class"),
       #          )
       #      )


