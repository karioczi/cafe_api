from rest_framework import serializers #type:ignore
from orders.models import Order, OrderItem
from orders.serializers.order_item.order_item_detail import OrderItemSerializer

class OrderCreateSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ['products', 'status', 'created_at', 'total_sum']
        read_only_fields = ['status', 'created_at']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        user = self.context['request'].user
        order = Order.objects.create(user=user, **validated_data)

        combined ={}
        for item_data in products_data:
            product = item_data['product']
            quantity = item_data['quantity']

            if quantity > product.quantity:
                raise serializers.ValidationError(
                    f'Not enough {product.name}, available {product.quantity}.'
                )
            
            if not product.is_active:
                raise serializers.ValidationError(
                    f'Product "{product.name}" is not available for ordering.'
                )

            if product in combined:
                combined[product] += quantity
            else:
                combined[product] = quantity

        for product, quantity in combined.items():
            product.quantity -= quantity
            product.save()

            price = product.price
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price_at_order=price
            )
        return order

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['products'] = OrderItemSerializer(
            instance.order_items.all(), many=True
        ).data
        return rep 