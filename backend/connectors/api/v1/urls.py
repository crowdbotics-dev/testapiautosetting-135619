from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135619ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135619", Testconnectors135619ViewSet, basename="testconnectors135619"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
