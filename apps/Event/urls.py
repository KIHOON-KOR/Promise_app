from django.urls import path
from apps.Event.views.event_create_view import EventCreateView

urlpatterns = [
    # 약속을 생성하는 주소
    path("", EventCreateView.as_view(), name="event_create"),
]
