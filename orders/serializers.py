from rest_framework import serializers
from orders.models import Order, OrderTrackingEvent


class OrderTrackingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTrackingEvent
        fields = ['status', 'timestamp', 'comment']
        read_only_fields = ['timestamp']


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    tracking_events = OrderTrackingEventSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'tracking_number', 'customer', 'status',
            'created_at', 'updated_at', 'tracking_events'
        ]
        read_only_fields = ['created_at', 'updated_at']


class OrderWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'tracking_number', 'customer', 'status']
        read_only_fields = ['customer']

    def validate(self, data):
        customer = data.get('customer')
        tracking_number = data.get('tracking_number')

        if self.instance is None:
            if Order.objects.filter(tracking_number=tracking_number).exists():
                raise serializers.ValidationError({
                    "tracking_number": (
                        "This customer already has an order with this tracking number."
                    )
                })

        return data

    def validate_status(self, new_status):
        """
        Validates the status transition of an order.
        """
        instance = self.instance
        if instance:
            current_status = instance.status

            if new_status == current_status:
                return new_status

            valid_transitions = {
                Order.Status.CREATED.value: Order.Status.PICKED.value,
                Order.Status.PICKED.value: Order.Status.DELIVERED.value,
                # No transitions out of DELIVERED
            }

            if new_status != valid_transitions.get(current_status):
                raise serializers.ValidationError(
                    f"Invalid status transition from '{current_status}' to '{new_status}'. "
                    f"Allowed transition from '{current_status}' is to "
                    f"'{valid_transitions.get(current_status, 'None')}'."
                )

        return new_status
