from django.shortcuts import render


def login_page(request):
    """로그인 화면(HTML)을 렌더링합니다."""
    return render(request, "user/login.html")