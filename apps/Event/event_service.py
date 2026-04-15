from apps.Event.models import Event
from apps.EventMember.models import EventMember


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
