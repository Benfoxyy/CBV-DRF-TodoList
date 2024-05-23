from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegistrationSerializer,CustomAuthTokenSerializer,CustomTokenObtainPairSerializer,ChangePasswordApiSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from mail_templated import send_mail

User = get_user_model()

class RegistrationApi(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                'email': serializer.validated_data['email']
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

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
    
class VerifideTestView(generics.GenericAPIView):
    def get(self, request,*args,**kwargs):
        send_mail('email/hello.tpl', {'name': 'admin'}, 'benxfoxy@gmail.com', ['hrvfurfgrfgurf@gmail.com'])
        return Response({'detail':'email sent'},status=status.HTTP_200_OK)