from rest_framework.serializers import ModelSerializer

from app.models import MLModels


class BaseUserSerializer(ModelSerializer):
    class Meta:
        model = MLModels
        fields = "__all__"
