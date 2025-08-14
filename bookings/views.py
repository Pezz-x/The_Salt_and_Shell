from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Booking

# Create your views here.

class BookingListView(ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'bookings/booking_detail.html'

class BookingCreateView(CreateView):
    model = Booking
    fields = ['customer', 'time_slot_id', 'party_size', 'special_requests']
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('booking-list')

class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['customer', 'time_slot_id', 'party_size', 'special_requests']
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('booking-list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'bookings/booking_confirm_delete.html'
    success_url = reverse_lazy('booking-list')
