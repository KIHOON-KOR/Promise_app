from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.User.serializers.login_serializer import UserLoginSerializer
from apps.User.services.login_service import LoginService

class UserLoginView(APIView):
    """클라이언트가 POST 방식으로 데이터를 전송할 때 실행되는 메서드"""

    @extend_schema(
        tags=["회원관리"],
        summary="로그인",
        request=UserLoginSerializer,
    )
    def post(self, request):
        # 1. 입력 데이터 검증
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 2. 서비스 레이어 호출
        result = LoginService.authenticate_user(serializer.validated_data)
        # 3. 서비스 레이어에서 성공적인 결과(토큰 데이터)가 돌아왔는지 확인
        if result:
            # 4. 성공했을 경우 클라이언트에게 보낼 응답 데이터를 구성하여 반환
            return Response(
                {
                    # 로그인이 성공했다는 안내 문구
                    "message": "로그인에 성공했습니다.",
                    # 발급받은 액세스 토큰을 응답 본문에 포함
                    "access": result['access'],
                    # 발급받은 리프레시 토큰을 응답 본문에 포함
                    "refresh": result['refresh']
                },
                status=status.HTTP_200_OK,
            )
        # 5. 인증 결과가 실패인 경우 실행되는 부분
        return Response(
            {"message": "아이디 또는 비밀번호가 잘못되었습니다."},
            status=status.HTTP_401_UNAUTHORIZED,
        )