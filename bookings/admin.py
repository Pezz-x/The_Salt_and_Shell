from django.contrib import admin
from .models import TimeSlot, Booking

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'is_available')
    list_filter = ('is_available', 'start_time')
    ordering = ('start_time',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'time_slot', 'party_size', 'booking_timestamp')
    search_fields = ('customer__name', 'special_requests')
    list_filter = ('booking_timestamp', 'party_size')
    ordering = ('-booking_timestamp',)
