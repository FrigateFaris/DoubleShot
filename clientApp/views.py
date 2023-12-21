from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView

from sellerApp.models import Category
from .forms import ClientRegistrationModelForm, ClientLoginModelForm, ProfileToUpdateModelForm, OrderModelForm
from .models import *


# Create your views here.
class ClientRegistrationPageView(CreateView):
    template_name = 'clientApp/registration_page.html'
    model = Client
    form_class = ClientRegistrationModelForm
    success_url = reverse_lazy('login_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ClientLogoutPageView(TemplateView):
    template_name = 'clientApp/logout_request.html'


def logout_client(request):
    logout(request)
    return redirect('start_page')


class ClientLoginPageView(LoginView):
    template_name = 'clientApp/login_page.html'
    form_class = ClientLoginModelForm

    def form_valid(self, form):
        super().form_valid(form)
        if self.request.user.is_staff is True:
            return redirect('category_list')
        elif self.request.user.is_courier is True:
            return redirect('courier_orders')
        return redirect('start_page')


class CategoryDetailPageView(DetailView):
    template_name = 'sellerApp/category_detail.html'
    model = Category
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.get_object()
        context['products_list'] = Product.objects.filter(category=category_name)
        return context


def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(client=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
        cart.save()
        return redirect(request.META.get('HTTP_REFERER', 'start_page'))
    else:
        return redirect('categories')


def change_quantity(request, item_id, action):
    item = get_object_or_404(CartItem, id=item_id)
    if action == 'increment':
        item.quantity += 1
        item.save()
    elif action == 'decrement':
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
    return redirect(request.META.get('HTTP_REFERER'))


class ProfilePageView(UpdateView, DetailView):
    template_name = 'clientApp/profile.html'
    model = Client
    form_class = ProfileToUpdateModelForm
    context_object_name = 'client'
    success_url = reverse_lazy('login_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(client=self.request.user)
            cart_items = CartItem.objects.filter(cart=cart)

            cart.general_price = sum(item.product.price * item.quantity for item in cart_items)
            cart.save()

            orders = Order.objects.filter(user=self.request.user).order_by('-order_date')
            context['cart'] = cart
            context['cart_item'] = cart_items
            context['orders'] = orders

            return context


class CurrentOrderPageView(CreateView):
    template_name = 'clientApp/order.html'
    form_class = OrderModelForm
    model = Order
    success_url = reverse_lazy('start_page')

    def form_valid(self, form):
        cart = get_object_or_404(Cart, client=self.request.user)

        if cart.cartitem_set.exists():
            order = form.save(commit=False)
            order.user = self.request.user.client
            order.total_price = cart.general_price
            order.save()

            for cart_item in cart.cartitem_set.all():
                order_item = OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )
                order_item.save()
            cart.cartitem_set.all().delete()
            return redirect('start_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        cart = Cart.objects.get(client=self.request.user)
        cart_items = CartItem.objects.filter(cart=cart).all()

        context['cart_items'] = cart_items
        context['cart'] = cart

        return context


class ConfirmationRequestPageView(TemplateView):
    template_name = 'clientApp/confirmation_order.html'


class OrderDetailPageView(DetailView, UpdateView):
    template_name = 'clientApp/order_detail.html'
    model = Order
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'order'
    form_class = OrderModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(user=self.request.user, slug=self.kwargs['slug'])
        order_items = OrderItem.objects.filter(order=order)

        context['order_item'] = order_items
        return context
