from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from apps.User.serializers.logout_serializer import UserLogoutSerializer


class UserLogoutView(APIView):
    """사용자의 로그아웃 요청을 처리하는 뷰 클래스를 선언"""

    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["회원관리"],
        summary="로그아웃",
        request=UserLogoutSerializer,
    )
    def post(self, request):
        # 1. 입력데이터 검증
        serializer = UserLogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            # 2. 클라이언트가 보낸 요청 데이터 중 리프레시 토큰 문자열을 찾아냄
            refresh_token = request.data["refresh"]
            # 3. 추출한 문자열을 코드로 조작 가능한 토큰 객체로 변환
            token = RefreshToken(refresh_token)
            # 4. 해당 토큰을 서버의 블랙리스트에 등록하여 더 이상 인증 수단으로 쓰지 못하게 만듬
            token.blacklist()
            # 5. 처리가 무사히 완료되면 성공 메시지와 함께 응답을 생성하여 반환
            return Response(
                {"message": "성공적으로 로그아웃 되었습니다."},
                status=status.HTTP_205_RESET_CONTENT,
            )

        # 6. 오류 발생 시
        except Exception as e:
            print(f"로그아웃 토큰 처리 에러: {e}")
            return Response(
                {"message": "유효하지 않은 토큰입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
