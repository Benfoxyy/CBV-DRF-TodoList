from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import (RegistrationSerializer,CustomAuthTokenSerializer,
                          CustomTokenObtainPairSerializer,ChangePasswordApiSerializer,ResendVerificationSerializer)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from mail_templated import EmailMessage
from ..utils import EmailThread
from django.shortcuts import get_object_or_404
import jwt
from jwt.exceptions import InvalidSignatureError,ExpiredSignatureError
from django.conf import settings


User = get_user_model()

class RegistrationApi(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data['email']
            serializer.save()
            user_obj = get_object_or_404(User,email=email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage('email/verification.tpl', {'token': token}, 'benxfoxy@gmail.com',to=[email])
            EmailThread(email_obj).start()

            return Response({'details':'verification code send'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get_tokens_for_user(self,user_obj):
        refresh = RefreshToken.for_user(user_obj)
        return str(refresh.access_token)
        

class CustomObtainToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
class DestroyToken(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ChangePasswordApi(generics.GenericAPIView):
    model = get_user_model()
    serializer_class = ChangePasswordApiSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        obj = self.request.user
        return obj
    
    def put(self,request,*args,**kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)
        

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password':['Wrong password']},status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            response = {'status':status.HTTP_200_OK,
                        'message':'Password successfully changed'
                        }
            return Response(response)
        return Response(status.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ResendVerification(generics.GenericAPIView):
    serializer_class = ResendVerificationSerializer
    def post(self, request, *args, **kwargs):
        serializer = ResendVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data['user']
        token = self.get_tokens_for_user(user_obj)
        message_obj = EmailMessage('email/verification.tpl', {'token': token}, 'benxfoxy@gmail.com',to=[user_obj.email])
        EmailThread(message_obj).start()
        return Response({'details': 'Verification token recend successfully'},status=status.HTTP_200_OK)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

class VerifyConf(APIView):
    def get(self,request,token,*args,**kwargs):
        try:
            token = (jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"]))
        except InvalidSignatureError:
            return Response({'detail':'Token is invalid'},status.HTTP_400_BAD_REQUEST) 
        except ExpiredSignatureError:
            return Response({'detail':'Token expired'},status.HTTP_400_BAD_REQUEST) 
        #if user_obj:=User.objects.get(pk=token.get('user_id')):
        user_obj = get_object_or_404(User,pk=token.get('user_id'))
        if user_obj.is_verified:
            return Response({'detail':'your account is already verified'},status=status.HTTP_400_BAD_REQUEST)
        user_obj.is_verified = True
        user_obj.save()
        return Response({'detail':'your verification successfully compleat!'},status=status.HTTP_201_CREATED)