from django.db import models
from apps.Event.models import Event
from django.conf import settings


class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="participated_events",
    )
    # 초대 권한 여부
    can_invite = models.BooleanField(default=False)
    # 삭제 동의 여부
    agree_delete = models.BooleanField(default=False)

    # 모델의 부가적인 설정을 담당하는 내부 클래스
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["event", "user"],
                name="unique_event_member",  # 데이터베이스에 저장될 제약조건의 이름을 명확하게 지정
            )
        ]

    # 객체를 문자열로 표현할 때 호출되는 기본 메서드
    def __str__(self):
        # 어떤 유저가 어떤 방에 있는지 알아보기 쉽게 출력
        return f"{self.user.username} in {self.event.title}"
