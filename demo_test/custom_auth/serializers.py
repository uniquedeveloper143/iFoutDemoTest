from django.contrib.auth import get_user_model
from rest_framework import serializers
from demo_test.custom_auth.models import ApplicationUser

User = get_user_model()


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class BaseUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = ApplicationUser
        fields = (
            'id', 'uuid', 'first_name', 'last_name','username', 'email', 'password')
        extra_kwargs = {
            'phone': {'write_only': True},
        }
        read_only_fields = ('uuid',)

    def save(self, **kwargs):
        password = self.validated_data.pop('password', None)

        user = super().save(**kwargs)
        if password:
            user.set_password(password)
            user.save(update_fields=['password'])
        return user


