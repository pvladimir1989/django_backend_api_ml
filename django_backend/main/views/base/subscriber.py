from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from main.models import Subscriber
from main.serializers.base import SubscriberSerializer


class SubscriberViewSet(ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = "__all__"
