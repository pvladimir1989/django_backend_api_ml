from rest_framework.serializers import ModelSerializer

from main.models import MLModels


class BaseUserSerializer(ModelSerializer):
    class Meta:
        model = MLModels
        fields = "__all__"
