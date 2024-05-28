from rest_framework import serializers

from apps.v1.worker.models import Unit


class UnitListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = [
            'pk',
            'name'
        ]


class VistCreateSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=255)
    unit_id = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
