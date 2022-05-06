
from django.urls import path,include
from rest_framework import routers
from .views import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls))
]