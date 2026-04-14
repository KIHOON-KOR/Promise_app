from rest_framework import serializers

from apps.User.models import User


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "nickname"]
        # 비밀번호 필드는 쓰기 전용으로 설정하여 데이터 조회 시에는 노출되지 않도록 보안을 강화
        extra_kwargs = {"password": {"write_only": True}}
