from rest_framework.serializers import ModelSerializer
from Administration.models import BidModel, ScheduleModel


class BidSerializer(ModelSerializer):
    class Meta:
        model = BidModel
        fields = ["data", "text"]


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = ScheduleModel
        fields = ["worker", "date", "time_from", "time_to", "delta"]
