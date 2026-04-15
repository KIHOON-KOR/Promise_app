from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.Event.event_serializer import EventMemberManageSerializer
from apps.Event.event_service import EventMemberService


class EventInviteView(APIView):
    """초대 기능만을 전담하는 뷰 클래스"""

    permission_classes = [IsAuthenticated]

    # API 문서에 초대 기능으로 명시합니다.
    @extend_schema(
        tags=["약속관리"], summary="약속 초대", request=EventMemberManageSerializer
    )
    def post(self, request, event_id):
        # 1. 입력데이터 검증
        serializer = EventMemberManageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 2. 검증된 대상 유저의 아이디를 가져옴
        target_user_id = serializer.validated_data["target_user_id"]
        # 3. 초대 서비스 로직을 실행
        success = EventMemberService.invite_user(event_id, target_user_id, request.user)

        # 4. 권한이 있어 초대가 성공한 경우
        if success:
            return Response(
                {"message": "성공적으로 초대했습니다."}, status=status.HTTP_200_OK
            )
        # 5. 초대 권한이 없어 실패한 경우
        return Response(
            {"message": "초대 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
        )
