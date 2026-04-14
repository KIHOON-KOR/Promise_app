from rest_framework import serializers

class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(
        help_text="로그인 시 발급받은 refresh 토큰을 입력하세요."
    )