from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('registration/',views.RegistrationApi.as_view(),name='registration'),
    path('change_password/',views.ChangePasswordApi.as_view(),name='change_pass'),
    path('token/login/',views.CustomObtainToken.as_view(),name='login-token'),
    path('token/logout/',views.DestroyToken.as_view(),name='logout-token'),
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(),name='create-token'),
    path('jwt/refresh/',TokenRefreshView.as_view(),name='refresh-token'),
]
