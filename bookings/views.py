from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime
from .models import Booking, TimeSlot
from .forms import BookingForm
from customers.models import Customer

#comment to delete
# Create your views here.

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'booking_detail.html'

# bookings/views.py
class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_create')

    def form_valid(self, form):
        # Ensure time slots exist for that date
        date = form.cleaned_data['date']
        if not TimeSlot.objects.filter(start_time__date=date).exists():
            TimeSlot.generate_slots_for_day(date)

        # Link or create customer
        customer, created = Customer.objects.get_or_create(
            email=form.cleaned_data['customer_email'],
            defaults={
                'name': form.cleaned_data['customer_name'],
                'phone_number': form.cleaned_data['customer_phone']
            }
        )

        booking = form.save(commit=False)
        booking.customer = customer
        booking.save()

        return super().form_valid(form)



class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['customer', 'time_slot', 'party_size', 'special_requests']
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')
