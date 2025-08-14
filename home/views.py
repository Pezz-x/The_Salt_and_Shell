from django.shortcuts import render

# Create your views here.
def home_page(request):
    """View for the home page"""
    return render(request, 'home.html')
