from django.conf import settings
from django.apps import apps

from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from orders.models import Order, OrderTrackingEvent
from orders.serializers import OrderSerializer, OrderWriteSerializer
from orders.permissions import IsOwnerOrAdmin

User = apps.get_model(settings.AUTH_USER_MODEL)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['customer__name', 'tracking_number']
    filterset_fields = ['status', 'customer']
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        if not user.is_staff and user.role != User.Roles.ADMIN:
            queryset = queryset.filter(customer=user)
        return queryset

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrderSerializer
        return OrderWriteSerializer

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_staff and user.role != User.Roles.ADMIN:
            serializer.validated_data['customer'] = user

        instance = serializer.save()
        OrderTrackingEvent.objects.create(
            order=instance,
            status=instance.status,
            comment=f"Order created with status '{instance.status}'."
        )

    def perform_update(self, serializer):
        original_instance = self.get_object()
        old_status = original_instance.status

        instance = serializer.save()

        if instance.status != old_status:
            OrderTrackingEvent.objects.create(
                order=instance,
                status=instance.status,
                comment=f"Status updated from '{old_status}' to '{instance.status}'."
            )

    def perform_destroy(self, instance):
        instance.delete()
        OrderTrackingEvent.objects.create(
            order=instance,
            status=instance.status,
            comment="Order soft-deleted."
        )
