from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
     path('sign_up/',views.Sign_Up.as_view(),name='sign_up'),
]
 