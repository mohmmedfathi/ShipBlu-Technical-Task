from django.db import models
from django.conf import settings
from core.models import SoftDeleteModel


class Order(SoftDeleteModel):
    class Status(models.TextChoices):
        CREATED = 'CREATED', 'Created'
        PICKED = 'PICKED', 'Picked'
        DELIVERED = 'DELIVERED', 'Delivered'

    tracking_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CREATED,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} (Customer ID: {self.customer_id})"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.tracking_number:
            self.tracking_number = f"ORD{self.id}"
            self.save(update_fields=['tracking_number'])
        
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderTrackingEvent(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='tracking_events'
    )
    status = models.CharField(
        max_length=20,
        choices=Order.Status.choices
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.order.tracking_number} - {self.status} at {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Order Tracking Event"
        verbose_name_plural = "Order Tracking Events"
