from django.urls import path
from apps.Event.views.event_create_view import EventCreateView
from apps.Event.views.event_invite_view import EventInviteView
from apps.Event.views.event_kick_view import EventKickView
from apps.Event.views.event_list_view import EventListView, EventAllListView
from apps.Event.views.event_permission_view import EventGrantPermissionView
from apps.Event.views.page_views import (
    create_promise,
    manage_promise,
    list_promise,
    detail_promise,
)

urlpatterns = [
    # 약속을 생성하는 주소
    path("", EventCreateView.as_view(), name="event_create"),
    # 약속을 조회하는 주소
    path("<int:event_id>/", EventListView.as_view(), name="event_list"),
    path("list/", EventAllListView.as_view(), name="event_all_list"),
    # 특정 약속에 누군가를 초대하는 주소
    path("<int:event_id>/invite/", EventInviteView.as_view(), name="event_invite"),
    # 특정 약속에서 누군가에게 초대 권한을 주는 주소
    path(
        "<int:event_id>/grant/",
        EventGrantPermissionView.as_view(),
        name="event_grant_permission",
    ),
    # 특정 약속에서 누군가를 강제로 내보내는 주소
    path("<int:event_id>/kick/", EventKickView.as_view(), name="event_kick"),
    # 브라우저 접속용
    path("create-page/", create_promise, name="create_page"),
    path("<int:event_id>/manage-page/", manage_promise, name="manage_page"),
    path("list-page/", list_promise, name="list_page"),
    # 특정 약속의 상세 화면을 보기 위해 접속할 주소 규칙을 명시합니다.
    path("<int:event_id>/detail-page/", detail_promise, name="detail_page"),
]
