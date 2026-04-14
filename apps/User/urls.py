from django.urls import path

from apps.User.views.signup_view import UserSignupView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
]