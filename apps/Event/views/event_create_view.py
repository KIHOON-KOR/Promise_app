from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.Event.event_serializer import EventCreateSerializer
from apps.Event.event_service import EventService


class EventCreateView(APIView):
    """약속 생성만을 전담하는 뷰 클래스"""
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["약속관리"],
        summary="약속 생성",
        request=EventCreateSerializer
    )

    def post(self, request):
        # 1. 입력데이터 검증
        serializer = EventCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 2. 통과된 데이터를 서비스 레이어로 넘겨 실제 약속을 만듬
        event = EventService.create_event(serializer.validated_data, request.user)

        return Response(
            {"message": "약속이 성공적으로 생성되었습니다."},
            status=status.HTTP_201_CREATED,
        )