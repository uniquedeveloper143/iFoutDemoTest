from rest_framework import viewsets
from django.contrib.auth import get_user_model, authenticate
from rest_framework.decorators import action
from demo_test.custom_auth.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from demo_test.custom_auth.permissions import IsSelf
from demo_test.utils.permissions import IsAPIKEYAuthenticated
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserAuthViewSet(viewsets.ViewSet):
    NEW_TOKEN_HEADER = 'token'
    permission_classes = (permissions.IsAuthenticated,)

    @classmethod
    def get_success_headers(cls, user):
        return {cls.NEW_TOKEN_HEADER: user.user_auth_tokens.create().key}

    def _auth(self, request, *args, **kwargs):
        auth_serializer = UserAuthSerializer(data=request.data, context={'request': request, 'view': self})
        auth_serializer.is_valid(raise_exception=True)

        user = authenticate(request, **auth_serializer.data)
        if not user:
            raise ValidationError('Invalid username or password, Please try again.')

        user_details = BaseUserSerializer(
            instance=user, context={'request': request, 'view': self}
        ).data
        user_details.update(self.get_success_headers(user))

        return Response(data=user_details, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, permission_classes=[permissions.AllowAny, IsAPIKEYAuthenticated],
            url_name='login', url_path='login')
    def classic_auth(self, request, *args, **kwargs):
        return self._auth(request, *args, for_agent=False, **kwargs)

    @action(methods=['delete'], detail=False, permission_classes=[permissions.IsAuthenticated, IsAPIKEYAuthenticated, IsSelf])
    def logout(self, request, *args, **kwargs):
        request.user.user_auth_tokens.all().delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

