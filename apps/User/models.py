from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    push_enabled = models.BooleanField(default=True)

    # 파이썬 객체를 문자열로 표현할 때 호출되는 기본 메서드
    def __str__(self):
        # 관리자 페이지 등에서 유저의 아이디가 출력되도록 설정
        return self.nickname
