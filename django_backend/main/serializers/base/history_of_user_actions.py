from rest_framework.serializers import ModelSerializer

from main.models import HistoryOfUserActions


class HistoryOfUserActionsSerializer(ModelSerializer):
    class Meta:
        model = HistoryOfUserActions
        fields = "__all__"
