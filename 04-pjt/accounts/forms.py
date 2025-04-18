from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.db import models

class CustomUserCreationForm(UserCreationForm):
    GENRE_CHOICES = [
        ('romance', '로맨스'),
        ('fantasy', '판타지'),
        ('sf', 'SF/공상 과학'),
        ('mystery', '미스터리 / 스릴러'),
        ('essay', '에세이'),
        ('poetry', '시'),
    ]

    genres = forms.MultipleChoiceField(
        choices=GENRE_CHOICES,
        required=True,
        help_text='하나 이상의 카테고리를 선택하세요',
        widget=forms.CheckboxSelectMultiple
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_image', 'phone_number', 'genres', 'author_status']




class CustomUserChangeForm(UserChangeForm):
    GENRE_CHOICES = [
        ('romance', '로맨스'),
        ('fantasy', '판타지'),
        ('sf', 'SF/공상 과학'),
        ('mystery', '미스터리 / 스릴러'),
        ('essay', '에세이'),
        ('poetry', '시'),
    ]
    genres = forms.MultipleChoiceField(
        choices=GENRE_CHOICES,
        required=True,
        help_text='하나 이상의 카테고리를 선택하세요',
        widget=forms.CheckboxSelectMultiple
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_image', 'phone_number', 'genres', 'author_status']
    
    

