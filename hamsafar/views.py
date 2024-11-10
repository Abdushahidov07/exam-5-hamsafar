from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView

from .models import Trip, Request, Application

def login(request):
    return redirect('/accounts/login/')

# CRUD для модели Trip
class TripListView(ListView):
    model = Trip
    template_name = 'home.html'
    context_object_name = 'trips'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Request.objects.all()
        return context
    
class TripDetailView(DetailView):
    model = Trip
    template_name = 'trip_detail.html'
    context_object_name = 'trip'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = self.get_object() 
        context['applications'] = Application.objects.filter(trip=trip)  # Все заявки на текущую поездку
        return context
    
class TripCreateView(CreateView):
    model = Trip
    template_name = 'trip_form.html'
    fields = ['start_location', 'end_location', 'departure_time', 'available_seats', 'price', 'description']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.driver = self.request.user
        return super().form_valid(form)

class TripUpdateView(UpdateView):
    model = Trip
    template_name = 'trip_form.html'
    fields = ['start_location', 'end_location', 'departure_time', 'available_seats', 'price', 'description']
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Trip.objects.filter(driver=self.request.user)

class TripDeleteView(DeleteView):
    model = Trip
    template_name = 'trip_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Trip.objects.filter(driver=self.request.user)

# CRUD для модели Request
class RequestListView(ListView):
    model = Request
    template_name = 'request_list.html'
    context_object_name = 'requests'


class RequestDetailView(DetailView):
    model = Request
    template_name = 'request_detail.html'
    context_object_name = 'request'

class RequestCreateView(CreateView):
    model = Request
    template_name = 'request_form.html'
    fields = ['start_location', 'description']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)

class RequestUpdateView(UpdateView):
    model = Request
    template_name = 'request_form.html'
    fields = ['start_location', 'description']
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Request.objects.filter(client=self.request.user)

class RequestDeleteView(DeleteView):
    model = Request
    template_name = 'request_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Request.objects.filter(client=self.request.user)

# CRUD для модели Application
class ApplicationListView(ListView):
    model = Application
    template_name = 'application_list.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(client=self.request.user)

class ApplicationCreateView(CreateView):
    model = Application
    template_name = 'application_form.html'
    fields = ['status',"start_location","description"] 
    success_url = reverse_lazy('application_list')

    def form_valid(self, form):
        trip = Trip.objects.filter(id=self.kwargs['pk']).first()
        form.instance.trip = trip
        form.instance.client = self.request.user
        
        return super().form_valid(form)

class ApplicationUpdateView(UpdateView):
    model = Application
    template_name = 'application_form.html'
    fields = ['status',"start_location","description"] 
    success_url = reverse_lazy('application_list')

    def get_queryset(self):
        return Application.objects.filter(client=self.request.user)

class ApplicationDeleteView(DeleteView):
    model = Application
    template_name = 'application_confirm_delete.html'
    success_url = reverse_lazy('application_list')

    def get_queryset(self):
        return Application.objects.filter(client=self.request.user)
