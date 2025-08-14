from django.shortcuts import render

# Create your views here.
def bookings_page(request):
    """View for the bookings page"""
    return render(request, 'bookings.html')
