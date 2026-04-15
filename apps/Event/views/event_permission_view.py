from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.Event.event_serializer import EventMemberManageSerializer
from apps.Event.event_service import EventMemberService


class EventGrantPermissionView(APIView):
    """권한 부여 기능만을 전담하는 뷰 클래스"""

    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["약속관리"], summary="초대 권한 부여", request=EventMemberManageSerializer
    )
    def post(self, request, event_id):
        # 1. 입력데이터 검증
        serializer = EventMemberManageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 2. 권한을 줄 대상의 아이디를 추출
        target_user_id = serializer.validated_data["target_user_id"]
        # 3. 권한 부여 서비스 로직 요청
        success = EventMemberService.grant_permission(
            event_id, target_user_id, request.user
        )

        # 4. 방장이 수행하여 성공한 경우
        if success:
            return Response(
                {"message": "초대 권한이 부여되었습니다."}, status=status.HTTP_200_OK
            )
        # 5. 방장이 아니라서 막힌 경우
        return Response(
            {"message": "권한 부여는 방장만 가능합니다."},
            status=status.HTTP_403_FORBIDDEN,
        )
