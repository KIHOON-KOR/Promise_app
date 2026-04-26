from django.contrib import admin
from django.urls import URLPattern, URLResolver, path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from django.conf import settings
from django.conf.urls.static import static

from apps.User.views.page_views import home_page

urlpatterns: list[URLPattern | URLResolver] = [
    path('', home_page, name='home'),
    path("admin/", admin.site.urls),
    path("api/v1/user/", include("apps.User.urls")),
    path("api/v1/event/", include("apps.Event.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    if "drf_spectacular" in settings.INSTALLED_APPS:
        urlpatterns += [
            # 1. 코드를 읽고 자동으로 스키마를 생성하는 뷰
            path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
            # 2. Swagger UI 설정 수정
            path(
                "api/schema/swagger-ui/",
                SpectacularSwaggerView.as_view(url_name="schema"),
                name="swagger-ui",
            ),
            path(
                "api/schema/redoc/",
                SpectacularRedocView.as_view(url_name="schema"),
                name="redoc",
            ),
        ]
