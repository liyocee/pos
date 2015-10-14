from rest_framework import serializers
from rest_auth.serializers import (
    TokenSerializer,
    PasswordResetSerializer
)
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from models import User


class UserSerializer(serializers.ModelSerializer):

    short_name = serializers.ReadOnlyField(source='get_short_name')
    full_name = serializers.ReadOnlyField(source='get_full_name')
    requires_password_change = serializers.ReadOnlyField()
    organization = serializers.DictField(
        read_only=True, source="get_organization")
    agent = serializers.DictField(
        read_only=True, source="get_agent")

    class Meta(object):
        model = User
        extra_kwargs = {'password': {'write_only': True}}


class UserAuthTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Token
        fields = ('key', 'user')


class UserPasswordResetSerializer(PasswordResetSerializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        # Check if user exists
        try:
            get_user_model().objects.get(email=value)
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError(
                {'user': ["{} does not exist".format(value)]})

    def save(self):
        email = self.initial_data['email']
        get_user_model().objects.get(email=email)
        """
            send password reset email/sms
        """
