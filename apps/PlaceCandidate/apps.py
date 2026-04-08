from django.apps import AppConfig


# Event 앱의 전반적인 설정을 관리하는 설정 클래스
class PlaceCandidate(AppConfig):
    # 데이터베이스에 데이터가 추가될 때 부여되는 고유 번호(기본키)의 타입을 자동으로 지정
    default_auto_field = "django.db.models.BigAutoField"
    # 장고가 이 앱을 정확히 찾을 수 있도록 폴더 경로를 포함한 전체 이름을 명시
    name = "apps.PlaceCandidate"
