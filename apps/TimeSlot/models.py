from django.db import models
from apps.EventMember.models import EventMember


class TimeSlot(models.Model):
    member = models.ForeignKey(
        EventMember, on_delete=models.CASCADE, related_name="time_slots"
    )
    # 약속 가능한 시작 시간을 날짜와 시간 형식으로 저장
    start_time = models.DateTimeField()
    # 약속 가능한 종료 시간을 날짜와 시간 형식으로 저장
    end_time = models.DateTimeField()

    # 객체를 문자열로 표현할 때 호출되는 기본 메서드
    def __str__(self):
        # 유저 이름과 등록한 시간대를 함께 출력
        return f"{self.member.user.username}: {self.start_time} ~ {self.end_time}"
