from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from main.models import HistoryOfUserActions
from main.serializers.base import HistoryOfUserActionsSerializer


class HistoryOfUserActionsViewSet(ModelViewSet):
    queryset = HistoryOfUserActions.objects.all()
    serializer_class = HistoryOfUserActionsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
