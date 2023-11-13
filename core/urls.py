from rest_framework import routers
from django.urls import path, include
from api.views.engineView import EngineView
from api.views.hoursView import HoursView
from api.views.proximityView import ProximityView
from api.views.rationView import RationView

router = routers.DefaultRouter()
router.register(r'engine', EngineView)
router.register(r'hours', HoursView)
router.register(r'proximity', ProximityView)
router.register(r'ration', RationView)

urlpatterns = [
    path('', include(router.urls)),
]
