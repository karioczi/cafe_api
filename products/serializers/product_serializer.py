from rest_framework import serializers #type:ignore[import]
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 
                  'name', 
                  'price', 
                  'description', 
                  'category'
        ]
        read_only_fields = ['id']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError(
                'Product name is required'
            )
        return value
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                'Product price can not be negative'
            )
        return value
    
    def validate(self, attrs):
        return attrs