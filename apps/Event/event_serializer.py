from rest_framework import serializers


class EventCreateSerializer(serializers.Serializer):
    """약속 생성을 위해 클라이언트가 보내는 데이터를 검증하는 클래스"""

    # 약속의 제목이 문자열 형태인지, 최대 길이를 넘지 않는지 검증
    title = serializers.CharField(max_length=100)
    # 비즈니스 목적 여부가 참/거짓 논리형인지 검증하며, 기본값은 거짓
    is_business = serializers.BooleanField(default=False)
