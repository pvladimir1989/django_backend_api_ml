from django.urls import path, include
from rest_framework import routers

from main.views import BaseUserViewSet, HistoryOfUserActionsViewSet, SubscriberViewSet, MLModelsViewSet

router = routers.DefaultRouter()
router.register(r'baseuser', BaseUserViewSet)
router.register(r'transactions', HistoryOfUserActionsViewSet)
router.register(r'subscribers', SubscriberViewSet)
router.register(r'mlmodels', MLModelsViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls
