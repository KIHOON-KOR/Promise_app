from django.db import models
from django.conf import settings


class Event(models.Model):
    title = models.CharField(max_length=100)
    is_business = models.BooleanField(default=False)
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="hosted_events"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # 객체를 문자열로 표현할 때 호출되는 기본 메서드
    def __str__(self):
        # 약속 객체를 조회할 때 약속의 제목이 보이도록 설정
        return self.title
