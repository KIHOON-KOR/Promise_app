from apps.User.models import User


class SignupService:
    def create_new_user(validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            nickname=validated_data.get('nickname', '')
        )

        return user