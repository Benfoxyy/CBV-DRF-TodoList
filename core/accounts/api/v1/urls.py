from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.RegistrationApi.as_view(),name='registration'),
    path('token/login/',views.CustomObtainToken.as_view(),name='login-token'),
    path('token/logout/',views.DestroyToken.as_view(),name='logout-token'),
]
