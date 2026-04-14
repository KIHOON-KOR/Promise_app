from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.User.serializers.signup_serializer import UserSignupSerializer
from apps.User.services.signup_service import SignupService


class UserSignupView(APIView):
    @extend_schema(
        tags=["회원관리"],
        summary="회원가입",
        request=UserSignupSerializer,
    )
    def post(self, request):
        # 1. 입력 데이터 검증
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 2. 서비스 레이어 호출
        user = SignupService.create_new_user(serializer.validated_data)

        return Response(
            {
                "message": "회원가입이 성공적으로 완료되었습니다.",
                "user": {"id": user.id, "username": user.username, "nickname": user.nickname},
            },
            status=status.HTTP_201_CREATED,
        )