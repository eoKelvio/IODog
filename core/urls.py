from rest_framework import routers
from django.urls import path, include
from api.views.hoursView import HoursView
from api.views.logView import LogView
from api.views.feedTimesView import FeedTimesView

router = routers.DefaultRouter()
router.register(r'hours', HoursView)
router.register(r'log', LogView)
router.register(r'feedTimes', FeedTimesView)



urlpatterns = [
    path('', include(router.urls)),
]
