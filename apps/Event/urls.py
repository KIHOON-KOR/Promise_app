from django.urls import path
from apps.Event.views.event_create_view import EventCreateView
from apps.Event.views.event_invite_view import EventInviteView

urlpatterns = [
    # 약속을 생성하는 주소
    path("", EventCreateView.as_view(), name="event_create"),
    # 특정 약속에 누군가를 초대하는 주소
    path("<int:event_id>/invite/", EventInviteView.as_view(), name="event_invite"),
]
