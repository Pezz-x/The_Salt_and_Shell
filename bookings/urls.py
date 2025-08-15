from django.urls import path
from .views import (
    BookingListView,
    BookingCreateView,
    BookingDetailView,
    BookingUpdateView,
    BookingDeleteView,
)

urlpatterns = [
    path('', BookingListView.as_view(), name='booking_list'),
    path('create/', BookingCreateView.as_view(), name='booking_create'),
    path('<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('<int:pk>/edit/', BookingUpdateView.as_view(), name='booking_update'),
    path('<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
]