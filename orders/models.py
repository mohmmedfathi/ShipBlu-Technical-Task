# orders/models.py
from django.db import models
from orders.managers import SoftDeleteModel 

# Create your models here.
class Customer(SoftDeleteModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, db_index=True) 

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Order(SoftDeleteModel):
    class Status(models.TextChoices):
        CREATED = 'CREATED', 'Created'
        PICKED = 'PICKED', 'Picked'
        DELIVERED = 'DELIVERED', 'Delivered'

    tracking_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')
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

    class Meta:
        ordering = ['-created_at']
        
class OrderTrackingEvent(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='tracking_events')
    status = models.CharField(max_length=20, choices=Order.Status.choices)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.order.tracking_number} - {self.status} at {self.timestamp}"
    
    class Meta:
        ordering = ['-timestamp']