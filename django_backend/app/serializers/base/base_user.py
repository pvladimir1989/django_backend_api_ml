from rest_framework.serializers import ModelSerializer

from app.models import BaseUser


class BaseUserSerializer(ModelSerializer):
    class Meta:
        model = BaseUser
        fields = "__all__"
