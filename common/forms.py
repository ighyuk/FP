from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    department = forms.CharField(label="학과")
    student_number = forms.CharField(label="학번")
    name = forms.CharField(label="이름")
    phone_number = forms.CharField(label="전화번호")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "department", "student_number", "name", "phone_number")
