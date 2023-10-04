from django.db import models
# Django 가 사용하는 default User 모델 기반으로 개발을 할거다
# 그래서 상속을 받음
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 앞으로도 필드 수정 동의 추가적인 작업을 하기 위해
# 상속을 받아서 정의
class User(AbstractUser):
    pass