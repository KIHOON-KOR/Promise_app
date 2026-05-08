from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.Event.event_serializer import EventListSerializer, EventAllListSerializer
from apps.Event.event_service import EventQueryService


class EventListView(APIView):
    """단일 약속 조회를 처리할 API 뷰 클래스를 선언"""

    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["약속조회"], summary="단일 약속 조회", responses=EventListSerializer
    )
    def get(self, request, event_id):
        """클라이언트가 데이터 조회를 위해 HTTP GET 방식으로 요청했을 때 실행되는 함수"""
        # 1. 서비스를 통해 요청받은 아이디의 약속 정보를 데이터베이스에서 가져옴
        event = EventQueryService.get_event(event_id)
        # 2. 가져온 데이터를 시리얼라이저에 넣어 변환을 시작
        serializer = EventListSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EventAllListView(APIView):
    """내 모든 약속 목록을 반환하는 API 뷰"""

    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["약속조회"],
        summary="내 모든 약속 목록 조회",
        responses=EventAllListSerializer(many=True),
    )
    def get(self, request):
        # 1. 서비스 로직을 호출하여 내가 연관된 모든 약속 데이터를 가져옴
        events = EventQueryService.get_all_user_events(request.user)
        # 2. 가져온 데이터를 시리얼라이저에 넣어 변환을 시작
        serializer = EventAllListSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
