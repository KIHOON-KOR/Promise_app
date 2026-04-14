from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    # 아이디 입력을 검증하기 위한 문자열 필드
    username = serializers.CharField()
    # 비밀번호를 검증하되 응답 데이터에는 노출되지 않도록 쓰기 전용으로 선언
    password = serializers.CharField(write_only=True)