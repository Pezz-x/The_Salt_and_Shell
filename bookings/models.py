from django.db import models
from customers.models import Customer
from datetime import datetime, timedelta, time
from django.utils.timezone import make_aware

# Create your models here.
class TimeSlot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        duration = (self.end_time - self.start_time).seconds // 3600
        return f"{self.start_time:%a %Y-%m-%d %H}:00 – {self.end_time:%H}:00 ({duration}hr)"

    @staticmethod
    def generate_slots_for_day(date):
        """
        Generates hourly slots from 5pm to 9pm for a given date.
        Returns list of created TimeSlot objects.
        """
        slots = []
        for hour in range(17, 22):  # 24 hour clock eg: 17 = 5pm, 22 = 10pm
            start_dt = make_aware(datetime.combine(date, time(hour)))
            end_dt = start_dt + timedelta(hours=1)
            slot, created = TimeSlot.objects.get_or_create(start_time=start_dt, end_time=end_dt)
            slots.append(slot)
        return slots
    

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT, related_name='bookings')
    party_size = models.PositiveIntegerField()
    booking_timestamp = models.DateTimeField(auto_now_add=True)
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer.name} - {self.time_slot} ({self.special_requests or 'No requests'})"
