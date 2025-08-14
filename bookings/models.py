from django.db import models
from customers.models import Customer

# Create your models here.
class TimeSlot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        duration = (self.end_time - self.start_time).seconds // 3600
        return f"{self.start_time:%a %Y-%m-%d %H}:00 – {self.end_time:%H}:00 ({duration}hr)"

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT, related_name='bookings')
    party_size = models.PositiveIntegerField()
    booking_timestamp = models.DateTimeField(auto_now_add=True)
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer.name} - {self.time_slot} ({self.special_requests or 'No requests'})"
