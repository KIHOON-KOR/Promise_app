from rest_framework import serializers

from apps.Event.models import Event


class EventCreateSerializer(serializers.Serializer):
    """약속 생성을 위해 클라이언트가 보내는 데이터를 검증하는 클래스"""

    # 약속의 제목이 문자열 형태인지, 최대 길이를 넘지 않는지 검증
    title = serializers.CharField(max_length=100)
    # 비즈니스 목적 여부가 참/거짓 논리형인지 검증하며, 기본값은 거짓
    is_business = serializers.BooleanField(default=False)


class EventMemberManageSerializer(serializers.Serializer):
    """약속 참여자를 관리(초대, 권한부여, 강퇴)할 때 필요한 데이터를 검증하는 클래스"""

    # 대상이 되는 유저의 고유 번호(ID)가 숫자 형태인지 검사하여 입력받음
    target_user_id = serializers.IntegerField()


class EventListSerializer(serializers.ModelSerializer):
    """조회 응답에 사용할 데이터를 검증하는 클래스"""

    class Meta:
        model = Event
        # 클라이언트에게 보여줄 항목들을 리스트로 지정
        fields = ["id", "title", "is_business", "host", "created_at"]


class EventAllListSerializer(serializers.ModelSerializer):
    """목록 조회를 위해 꼭 필요한 필드만 선택하여 간결하게 구성한 클래스"""

    # 방장의 정보를 단순히 아이디 숫자가 아닌 이름(username)으로 보여주기 위해 추가
    host_name = serializers.CharField(source="host.username", read_only=True)

    class Meta:
        model = Event
        # 클라이언트에게 보여줄 항목들을 리스트로 지정
        fields = ["id", "title", "host_name", "is_business", "created_at"]
