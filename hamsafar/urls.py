from django.urls import path
from .views import *
urlpatterns = [
    path("", login, name="login"),

    # Trip URLs
    path('trips/', TripListView.as_view(), name='home'),
    path('trip/<int:pk>/', TripDetailView.as_view(), name='trip_detail'),
    path('trip/new/', TripCreateView.as_view(), name='trip_create'),
    path('trip/<int:pk>/edit/', TripUpdateView.as_view(), name='trip_update'),
    path('trip/<int:pk>/delete/', TripDeleteView.as_view(), name='trip_delete'),

    # Request URLs
    path('requests/', RequestListView.as_view(), name='request_list'),
    path('request/<int:pk>/', RequestDetailView.as_view(), name='request_detail'),
    path('request/new/', RequestCreateView.as_view(), name='request_create'),
    path('request/<int:pk>/edit/', RequestUpdateView.as_view(), name='request_update'),
    path('request/<int:pk>/delete/', RequestDeleteView.as_view(), name='request_delete'),

    # Application URLs
    path('applications/', ApplicationListView.as_view(), name='application_list'),
    path('application/<int:pk>/new/', ApplicationCreateView.as_view(), name='application_create'),
    path('application/<int:pk>/edit/', ApplicationUpdateView.as_view(), name='application_update'),
    path('application/<int:pk>/delete/', ApplicationDeleteView.as_view(), name='application_delete'),
]
