from django import forms
from .models import Booking, TimeSlot
from customers.models import Customer

class BookingForm(forms.ModelForm):
    customer_name = forms.CharField(max_length=100)
    customer_email = forms.EmailField()
    customer_phone = forms.CharField(max_length=20)
    date = forms.DateField(widget=forms.SelectDateWidget)
    time_slot = forms.ModelChoiceField(queryset=TimeSlot.objects.all())

    class Meta:
        model = Booking
        fields = [
            'customer_name', 'customer_email', 'customer_phone',
            'time_slot', 'party_size', 'special_requests'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
