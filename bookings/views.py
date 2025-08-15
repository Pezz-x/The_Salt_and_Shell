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

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_list')

    def form_valid(self, form):
        # Ensure time slots exist for that date
        date = form.cleaned_data['date']
        if not TimeSlot.objects.filter(start_time__date=date).exists():
            TimeSlot.generate_slots_for_day(date)

        # Capacity check
        MAX_COVERS = 40  # change this to your restaurant's capacity
        slot = form.cleaned_data['time_slot']
        current_covers = Booking.objects.filter(time_slot=slot).aggregate(
            total=models.Sum('party_size')
        )['total'] or 0

        if current_covers + form.cleaned_data['party_size'] > MAX_COVERS:
            form.add_error('party_size', f"Sorry, we only have {MAX_COVERS - current_covers} seats left for that time.")
            return self.form_invalid(form)

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
