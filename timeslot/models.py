from django.db import models


# Create your models here.
class TimeSlot(models.Model):
    time_slot_date = models.DateField()
    time_slot_hour = models.TimeField()
    total_capacity = models.IntegerField(default=40)
    capacity_taken = models.IntegerField(default=0)

    class Meta:
        unique_together = ('time_slot_date', 'time_slot_hour')

    def available_capacity(self):
        return self.total_capacity - self.capacity_taken

    def __str__(self):
        return (
            f"{self.time_slot_date} at {self.time_slot_hour} "
            f"({self.available_capacity()} seats left)"
        )
