from django.test import TestCase
from django.utils.timezone import make_aware
from datetime import date, time, datetime, timedelta

from bookings.models import TimeSlot, Booking
from customers.models import Customer


class TimeSlotModelTests(TestCase):
    def test_generate_slots_for_day_creates_expected_slots(self):
        test_date = date(2025, 8, 19)
        slots = TimeSlot.generate_slots_for_day(test_date)

        self.assertEqual(len(slots), 5)  # 5pm to 9pm = 5 slots
        expected_hours = list(range(17, 22))
        for slot, hour in zip(slots, expected_hours):
            self.assertEqual(slot.start_time.hour, hour)
            self.assertEqual(slot.end_time.hour, hour + 1)
            self.assertTrue(slot.is_available)

    def test_generate_slots_for_day_idempotency(self):
        test_date = date(2025, 8, 19)
        slots_first = TimeSlot.generate_slots_for_day(test_date)
        slots_second = TimeSlot.generate_slots_for_day(test_date)

        self.assertEqual(len(slots_first), 5)
        self.assertEqual(len(slots_second), 5)
        self.assertEqual(set(slots_first), set(slots_second))  # Should not duplicate


class BookingModelTests(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="Alice Example")
        self.slot = TimeSlot.generate_slots_for_day(date.today())[0]

    def test_booking_creation(self):
        booking = Booking.objects.create(
            customer=self.customer,
            time_slot=self.slot,
            party_size=4,
            special_requests="Window seat"
        )

        self.assertEqual(booking.customer.name, "Alice Example")
        self.assertEqual(booking.time_slot, self.slot)
        self.assertEqual(booking.party_size, 4)
        self.assertEqual(booking.special_requests, "Window seat")
        self.assertIsNotNone(booking.booking_timestamp)

    def test_booking_str_representation(self):
        booking = Booking.objects.create(
            customer=self.customer,
            time_slot=self.slot,
            party_size=2
        )
        expected_str = f"{self.customer.name} - {self.slot} (No requests)"
        self.assertEqual(str(booking), expected_str)