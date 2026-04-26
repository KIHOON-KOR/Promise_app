from django.shortcuts import render


def login_page(request):
    """로그인 화면(HTML)을 렌더링합니다."""
    return render(request, "user/login.html")

def signup_page(request):
    """회원가입 화면(HTML)을 렌더링합니다."""
    return render(request, "user/signup.html")

def my_page(request):
    """마이페이지 화면(HTML)을 렌더링합니다."""
    return render(request, "user/mypage.html")

def home_page(request):
    return render(request, "home.html")