
from django.urls import path,include
from rest_framework import routers
from .views import StudentViewSet,ExpenseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'expense', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls))
]