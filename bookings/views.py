from django.shortcuts import render

# Create your views here.
def bookings_page(request):
    """View for the bookings page"""
    return render(request, 'booking_form.html')

def view_bookings(request):
    """View for viewing all bookings"""
    return render(request, 'booking_list.html')
