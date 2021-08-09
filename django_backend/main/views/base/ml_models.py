from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from main.models import MLModels
from main.serializers.base import MLModelsSerializer


class MLModelsViewSet(ModelViewSet):
    queryset = MLModels.objects.all()
    serializer_class = MLModelsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = "__all__"
