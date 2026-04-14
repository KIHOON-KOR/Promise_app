from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class LoginService:
    """사용자의 아이디와 비밀번호를 받아 검증하는 메서드"""

    def authenticate_user(validated_data):
        # 장고 내부의 인증 시스템을 호출하여 사용자 존재 여부와 비밀번호 일치를 확인
        user = authenticate(
            username=validated_data["username"], password=validated_data["password"]
        )
        # 인증된 사용자 객체가 정상적으로 반환되었는지 검사하는 조건문
        if user:
            # JSON Web Token(리프레시 토큰 및 액세스 토큰)을 새로 생성
            refresh = RefreshToken.for_user(user)
            # 생성된 토큰 정보와 사용자 객체를 딕셔너리로 묶어 반환 준비
            return {
                # 액세스 토큰을 추출하고 문자열로 형변환하여 딕셔너리에 담기
                "access": str(refresh.access_token),
                # 리프레시 토큰 자체도 문자열로 형변환하여 딕셔너리에 함께 담기
                "refresh": str(refresh),
                # 후속 처리에서 활용할 수 있도록 인증된 사용자 객체도 담음
                "user": user,
            }
        return None
