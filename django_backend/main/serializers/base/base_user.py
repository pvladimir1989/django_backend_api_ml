from rest_framework.serializers import ModelSerializer

from main.models import BaseUser


class BaseUserSerializer(ModelSerializer):
    class Meta:
        model = BaseUser
        fields = "__all__"
