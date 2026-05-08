from django.shortcuts import render


def create_promise(request):
    """약속생성 페이지(HTML)를 렌더링합니다."""
    return render(request, "event/create.html")


def manage_promise(request):
    """약속관리 페이지(HTML)를 렌더링합니다."""
    return render(request, "event/manage.html")


def list_promise(request):
    """전체 약속 목록 페이지(HTML)를 연결해주는 함수를 정의"""
    return render(request, "event/list.html")


def detail_promise(request, event_id):
    """단일 약속 상세 페이지(HTML)를 연결해주는 함수를 정의"""
    return render(request, "event/detail.html")
