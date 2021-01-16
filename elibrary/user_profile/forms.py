from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.modelfields import PhoneNumberField


class ProfileForm(forms.ModelForm):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=8)
    registration_number = models.CharField(max_length=8)
    hall_number = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(14)])
    room_number = models.PositiveIntegerField(validators=[MinValueValidator(101), MaxValueValidator(999)])
    mobile = PhoneNumberField(blank=False, null=False)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'roll_number', 'registration_number', 'hall_number', 'room_number',
                  'mobile')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Mandatory')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)