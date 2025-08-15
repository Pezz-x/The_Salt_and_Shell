from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Booking
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
        # Try to get existing customer or create a new one
        customer, created = Customer.objects.get_or_create(
            email=form.cleaned_data['customer_email'],
            defaults={
                'name': form.cleaned_data['customer_name'],
                'phone_number': form.cleaned_data['customer_phone']
            }
        )

        # Optional flash message if customer already exists
        if not created:
            messages.info(
                self.request,
                f"Welcome back, {customer.name}! We’ve used your existing profile."
            )

        # Create booking linked to customer
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
