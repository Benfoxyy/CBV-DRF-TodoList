from typing import Dict
from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegistrationSerializer(serializers.ModelSerializer):
    conf_pass = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'conf_pass']
    
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('conf_pass'):
            raise serializers.ValidationError({'detail': 'password doesnt match!'})
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('conf_pass', None)
        return User.objects.create_user(**validated_data)
    

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
            if not user.is_verified:
                raise serializers.ValidationError({'detail':'user is not verifide'})
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validatad_data = super().validate(attrs)
        if not self.user.is_verified:
                raise serializers.ValidationError({'detail':'user is not verifide'})
        validatad_data['email'] = self.user.email
        validatad_data['user_id'] = self.user.id
        return validatad_data
    
class ChangePasswordApiSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True)
    new_password_conf = serializers.CharField(required = True)

    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('new_password_conf'):
            raise serializers.ValidationError({'detail':'password doesnt match!'})
        try:
            validate_password(attrs.get('new_password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'new_password':list(e.messages)})
        return super().validate(attrs)