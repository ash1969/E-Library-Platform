from django import forms
from .models import *


class SearchForm(forms.ModelForm):
    Title = forms.CharField(max_length=100, required=False)
    Author = forms.CharField(max_length=100, required=False)
    department_choices = (
        ('Biotechnology', 'Biotechnology'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Chemical Engineering', 'Chemical Engineering'),
        ('Computer Science & Engineering', 'Computer Science & Engineering'),
        ('Chemistry', 'Chemistry'),
        ('Electronics & Communication Engineering', 'Electronics & Communication Engineering'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Earth & Environmental Studies', 'Earth & Environmental Studies'),
        ('Humanities & Social Sciences', 'Humanities & Social Sciences'),
        ('Mathematics', 'Mathematics'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Metallurgical & Materials Engineering', 'Metallurgical & Materials Engineering'),
        ('Management Studies', 'Management Studies'),
        ('Physics', 'Physics'),
    )
    department = models.CharField(max_length=100, choices=department_choices, blank=True, null=True)
    type_choices = (
        ('Course Book', 'Course Book'),
        ('Reference Book', 'Reference Book'),
        ('Others', 'Others'),
    )
    type = models.CharField(max_length=100, choices=type_choices, blank=True, null=True)

    class Meta:
        model = ECopies
        fields = ('department', 'type')