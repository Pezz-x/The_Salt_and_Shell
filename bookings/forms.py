from django import forms
from .models import Booking
from customers.models import Customer

class BookingForm(forms.ModelForm):
    customer_name = forms.CharField(max_length=100)
    customer_email = forms.EmailField()
    customer_phone = forms.CharField(max_length=20)

    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'customer_phone', 'time_slot', 'party_size', 'special_requests']
