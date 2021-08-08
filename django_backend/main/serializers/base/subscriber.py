from rest_framework.serializers import ModelSerializer

from main.models import Subscriber


class SubscriberSerializer(ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"
