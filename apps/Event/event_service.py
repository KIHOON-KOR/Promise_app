from apps.Event.models import Event
from apps.EventMember.models import EventMember
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

class EventService:
    """약속 자체와 관련된 핵심 로직을 담당하는 서비스 클래스"""

    def create_event(validated_data, user):
        # 1. 전달받은 검증된 데이터와 요청한 유저를 방장으로 설정하여 약속 데이터를 만듬
        event = Event.objects.create(
            # 딕셔너리에서 제목 값을 추출해 저장
            title=validated_data["title"],
            # 딕셔너리에서 비즈니스 여부를 추출하며, 없으면 거짓을 대입
            is_business=validated_data.get("is_business", False),
            # 약속을 만든 현재 사용자를 방장으로 지정
            host=user,
        )
        # 2. 방장 본인을 약속의 첫 번째 멤버로 등록하며, 초대 권한을 부여
        EventMember.objects.create(event=event, user=user, can_invite=True)
        return event

class EventMemberService:
    """약속 내부의 참여자들을 관리하는 로직을 담당하는 서비스 클래스"""

    def invite_user(event_id, target_user_id, request_user):
        # 1. 전달받은 아이디로 약속을 찾고, 없으면 에러를 발생시킴
        event = get_object_or_404(Event, id=event_id)
        # 2. 초대를 요청한 사람이 해당 약속에 소속되어 있는지 확인
        inviter = get_object_or_404(EventMember, event=event, user=request_user)
        # 3. 요청자가 방장이거나, 멤버십 속성에 초대 권한이 있는지 검사
        if event.host == request_user or inviter.can_invite:
            # 장고 프로젝트에 설정된 기본 회원 모델을 불러옴
            User = get_user_model()
            # 대상 유저 객체를 데이터베이스에서 찾아냄
            target_user = get_object_or_404(User, id=target_user_id)
            # 대상 유저를 해당 약속의 멤버로 새롭게 등록
            EventMember.objects.create(event=event, user=target_user)
            return True
        return False