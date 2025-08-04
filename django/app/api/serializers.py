from rest_framework import serializers
from .models import VariantHeader, VariantItem, VariantItemValue


class VariantHeaderSerializer(serializers.ModelSerializer):
  class Meta:
    model = VariantHeader
    fields = '__all__'
    
class VariantItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = VariantItem
    fields = '__all__'
    
class VariantItemValue(serializers.ModelSerializer):
  class Meta:
    model = VariantItemValue
    fields = '__all__'