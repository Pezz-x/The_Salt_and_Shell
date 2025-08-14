from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings_page, name='bookings'),
    path('view-bookings/', views.view_bookings, name='view-bookings'),
]
