from django.urls import path,include
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.Todolist.as_view(),name= 'home'),
    path('add/', views.Add.as_view(),name= 'add'),
    path('edit/<int:pk>/', views.Edit.as_view(),name= 'edit'),
    path('delete/<int:pk>/', views.Delete.as_view(),name= 'delete'),
    path('api/v1/', include('main.api.v1.urls'))
]
