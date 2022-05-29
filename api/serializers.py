from .models import Employee, PointOfSale, Visit
from rest_framework import serializers


class PointOfSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfSale
        fields = ['id', 'title']


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'datatime', 'latitude', 'longitude']

    def create(self, validated_data):
        validated_data['point_sale_id'] = self.context['pk']
        validated_data['visitor'] = self.context['visitor']
        return Visit.objects.create(**validated_data)
