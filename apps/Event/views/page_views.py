from django.shortcuts import render


def create_promise(request):
    """약속생성 페이지(HTML)를 렌더링합니다."""
    return render(request, "event/create.html")
