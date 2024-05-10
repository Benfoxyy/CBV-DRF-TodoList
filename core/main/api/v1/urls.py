from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()

router.register('todo',views.ListModelViewSet,basename = 'task')

urlpatterns = router.urls
