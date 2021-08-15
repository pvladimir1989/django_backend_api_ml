from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from main.models import BaseUser
from main.serializers.base import BaseUserSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class BaseUserViewSet(ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ['loan_amount']
    search_fields = ['education', 'property_area']
    ordering_fields = ['loan_amount', 'loan_amount_term']
