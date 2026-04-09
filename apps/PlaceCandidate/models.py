from django.db import models
from apps.Event.models import Event


class PlaceCandidate(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="place_candidates"
    )
    place_name = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    vote_count = models.IntegerField(default=0)

    # 객체를 문자열로 표현할 때 호출되는 기본 메서드
    def __str__(self):
        # 객체를 조회할 때 장소의 이름이 보이도록 설정
        return self.place_name
