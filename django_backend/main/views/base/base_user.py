from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from main.models import BaseUser
from main.serializers.base import BaseUserSerializer


class BaseUserViewSet(ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['loan_amount']
