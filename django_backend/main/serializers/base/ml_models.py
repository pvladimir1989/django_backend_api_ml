from rest_framework.serializers import ModelSerializer

from main.models import MLModels


class MLModelsSerializer(ModelSerializer):
    class Meta:
        model = MLModels
        fields = "__all__"
