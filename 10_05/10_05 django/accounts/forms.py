from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# Django 가 제공하는 CreationForm 을 상속받아서
# 우리가 정의한 User 모델을 사용하도록 새로 생성

class CustomCreationForm(UserCreationForm):
    # 추가할 필드 정의
    nickname = forms.CharField(max_length=30, required=False, help_text="필수아님")
    class Meta(UserCreationForm.Meta):
        # get_user_model() : 현재 프로젝트에 세팅된 User 모델을 가져오는 역할
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('nickname',)
