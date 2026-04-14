from django.urls import path

from apps.User.views.login_view import UserLoginView
from apps.User.views.logout_view import UserLogoutView
from apps.User.views.signup_view import UserSignupView
from apps.User.views.withdrawal_view import UserWithdrawalView

urlpatterns = [
    path("signup/", UserSignupView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path('withdrawal/', UserWithdrawalView.as_view(), name='withdrawal'),
]
