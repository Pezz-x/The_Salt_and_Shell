from django import forms
from .models import Booking, TimeSlot
from customers.models import Customer

class BookingForm(forms.ModelForm):
    customer_name = forms.CharField(max_length=100)
    customer_email = forms.EmailField()
    customer_phone = forms.CharField(max_length=20)
    date = forms.DateField(widget=forms.SelectDateWidget)
    time_slot = forms.ModelChoiceField(queryset=TimeSlot.objects.none())

    class Meta:
        model = Booking
        fields = [
            'customer_name', 'customer_email', 'customer_phone',
            'date', 'time_slot', 'party_size', 'special_requests'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If date is pre-filled, filter slots for that date
        if 'date' in self.data:
            try:
                date_val = self.data.get('date')
                # date_val is "YYYY-MM-DD"
                from datetime import datetime
                parsed_date = datetime.strptime(date_val, "%Y-%m-%d").date()
                self.fields['time_slot'].queryset = TimeSlot.objects.filter(start_time__date=parsed_date, is_available=True)
            except ValueError:
                pass
        elif self.instance.pk:
            self.fields['time_slot'].queryset = TimeSlot.objects.filter(start_time__date=self.instance.time_slot.start_time.date())
