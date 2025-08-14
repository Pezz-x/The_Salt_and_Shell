from django.db import models
from customers.models import Customer

# Create your models here.
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')
    time_slot_id = models.IntegerField()
    party_size = models.PositiveIntegerField()
    booking_timestamp = models.DateTimeField(auto_now_add=True)
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer.name} - {self.time_slot_id} ({self.special_requests or 'No requests'})"
