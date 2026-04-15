from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.Event.event_serializer import EventMemberManageSerializer
from apps.Event.event_service import EventMemberService


class EventKickView(APIView):
    """멤버 강퇴 기능만을 전담하는 뷰 클래스"""
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=["약속관리"], summary="멤버 강퇴", request=EventMemberManageSerializer)
    def post(self, request, event_id):
        # 1. 입력데이터 검증
        serializer = EventMemberManageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 2. 권한을 줄 대상의 아이디를 추출
        target_user_id = serializer.validated_data["target_user_id"]
        # 3. 권한 부여 서비스 로직 요청
        success = EventMemberService.kick_user(
            event_id, target_user_id, request.user
        )

        # 4. 강퇴에 성공했을 경우
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        # 5. 거절된 경우
        return Response({"message": "강퇴는 방장만 가능합니다."}, status=status.HTTP_403_FORBIDDEN)