from django.urls import path
from .views import (
    BookingListView,
    BookingDetailView,
    BookingCreateView,
    BookingUpdateView,
    BookingDeleteView,
)

urlpatterns = [
    path('', BookingListView.as_view(), name='booking-list'),
    path('<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('create/', BookingCreateView.as_view(), name='booking-create'),
    path('<int:pk>/edit/', BookingUpdateView.as_view(), name='booking-update'),
    path('<int:pk>/delete/', BookingDeleteView.as_view(), name='booking-delete'),
]
