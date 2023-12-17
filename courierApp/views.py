from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, ListView

from clientApp.models import Order, OrderItem
from sellerApp.forms import OrderSellerModelForm


# Create your views here.
def order_accepted(request, slug):
    order = Order.objects.get(slug=slug)
    order.status = 'Принято'
    order.courier = request.user
    order.save()
    return redirect('courier_orders')


def order_delivered(request, slug):
    order = Order.objects.get(slug=slug)
    order.status = 'Доставлено'
    order.save()
    return redirect('current_courier_orders')


class CourierOrdersPageView(ListView):
    template_name = 'courierApp/current_courier_orders.html'
    model = Order

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        courier_orders = Order.objects.filter(courier=self.request.user)
        print(self.request.user)

        context['courier_orders'] = courier_orders
        return context
