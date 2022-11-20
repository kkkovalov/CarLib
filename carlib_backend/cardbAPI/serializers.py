from rest_framework import serializers
from cardbAPI.models import Manufacturers, Models

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manufacturers
        fields=('manufactureId','manufactureName','manufactureYearFounded','manufactureHeadquarters')

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Models
        fields=('modelId','manufactureName','modelName')