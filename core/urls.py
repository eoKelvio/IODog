from rest_framework import routers
from django.urls import path, include
from api.views.views import CategoryView

router = routers.DefaultRouter()
router.register(r'', CategoryView)

urlpatterns = [
    path('', include(router.urls)),
]
