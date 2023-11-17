from rest_framework import serializers
from .models import DepositProducts, DepositOptions


class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'


class DepositOptionsSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source = "product_id")
    class Meta:
        model = DepositOptions
        fields = '__all__'
