from rest_framework import serializers #type:ignore[import]
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name', 
            'price', 
            'description', 
            'available',
            'category',
            'quantity',
            'created_at',
            'updated_at',
            'is_active',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError(
                'Product name is required.'
            )
        return value
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                'Product price can not be negative.'
            )
        return value
    
    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError(
                'Description is required.'
            )
        return value

    def validate_category(self, value):  
        if not value:
            raise serializers.ValidationError(
                'Category is required.'
            )
        return value
        
    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError(
                'Quantity can not be negative.'
            )
        return value
    
    def validate(self, attrs):
        return attrs