from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from django.utils import timezone


class UserWithdrawalView(APIView):
    """회원 탈퇴 요청을 처리하기 위한 뷰 클래스"""

    permission_classes = [IsAuthenticated]

    @extend_schema(tags=["회원관리"], summary="회원탈퇴")
    def delete(self, request):
        # 1. 액세스 토큰을 통해 신원이 확인된 사용자 객체를 요청 데이터에서 꺼내옴
        user = request.user

        # 2. 사용자 객체의 활성화 상태 속성을 거짓(False)으로 바꾸어 논리적 삭제 처리
        user.is_active = False

        # 3. 탈퇴 처리가 진행되는 현재 시간을 숫자로 이루어진 초 단위 값(타임스탬프)으로 변환
        current_time = int(timezone.now().timestamp())

        # 4. 삭제되었음을 알리는 문구, 현재 시간, 유저의 고유 번호를 엮어 새로운 아이디를 만듬
        user.username = f"deleted_{current_time}_{user.id}"

        # 5. 닉네임 역시 나중에 다른 사람이 사용할 수 있도록 임의의 문자열로 덮어써서 자리를 비워줌
        user.nickname = f"deleted_{current_time}_{user.id}"

        # 6. 변경된 활성 상태 속성을 데이터베이스에 최종적으로 기록하고 저장
        user.save()

        return Response(
            {"message": "회원 탈퇴가 완료되었습니다."},
            status=status.HTTP_204_NO_CONTENT,
        )
