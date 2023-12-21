from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView

from clientApp.forms import OrderModelForm
from clientApp.models import Cart, Order, OrderItem
from .forms import UpdateProductModelForm, CreateProductModelForm, OrderSellerModelForm, CategoryCreateModelForm, \
    BrandCreateModelForm
from .models import *


# Create your views here.
class StartPageView(ListView):
    template_name = 'sellerApp/index.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_last'] = Product.objects.all().order_by('-id')[:6]
        return context


class AlcoholCategoryListPageView(ListView):
    template_name = 'sellerApp/alcohol_category_list.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_last'] = Product.objects.all().order_by('-id')[:12]
        context['category_list'] = Category.objects.all()
        return context


class AlcoholCategoryDetailPageView(DetailView):
    template_name = 'sellerApp/category_detail.html'
    model = Category
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.get_object()
        product_list = Product.objects.filter(category=category_name)
        paginator = Paginator(product_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            product_list = paginator.page(page)
        except PageNotAnInteger:
            product_list = paginator.page(1)
        except EmptyPage:
            product_list = paginator.page(paginator.num_pages)
        context['products_list'] = product_list
        return context


class ProductDetailPageView(DetailView):
    template_name = 'sellerApp/product_detail.html'
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'product'


class RequestToDeleteProductPageView(TemplateView):
    template_name = 'sellerApp/product_delete.html'


class DeleteProductPageView(DeleteView):
    template_name = 'sellerApp/product_delete.html'
    model = Product
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('category_list')


class UpdateProductPageView(UpdateView):
    template_name = 'sellerApp/update_product.html'
    model = Product
    form_class = UpdateProductModelForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'product'
    success_url = reverse_lazy('success_updating')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SuccessUpdatingPageView(TemplateView):
    template_name = 'sellerApp/success_updating.html'


class CreateProductPageView(CreateView):
    template_name = 'sellerApp/create_product.html'
    model = Product
    form_class = CreateProductModelForm
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class OrdersListPageView(ListView):
    template_name = 'sellerApp/orders_list.html'
    model = Order

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        orders = Order.objects.all().order_by('-order_date')

        context['orders'] = orders
        return context


class OrderSellerDetailPageView(DetailView, UpdateView):
    template_name = 'clientApp/order_detail.html'
    model = Order
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'order'
    form_class = OrderSellerModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(slug=self.kwargs['slug'])
        order_items = OrderItem.objects.filter(order=order)

        context['order_item'] = order_items
        return context


def order_denied_status(request, slug):
    order = Order.objects.get(slug=slug)
    order.status = 'Отказано'
    order.save()
    return redirect('orders_list')


def order_approved_status(request, slug):
    order = Order.objects.get(slug=slug)
    order.status = 'Одобренно'
    order.save()
    return redirect('orders_list')


class CategoryCreatePageView(CreateView):
    template_name = 'sellerApp/category_create.html'
    model = Category
    form_class = CategoryCreateModelForm
    success_url = reverse_lazy('category_list')


class BrandCreatePageView(CreateView):
    template_name = 'sellerApp/category_create.html'
    model = Category
    form_class = BrandCreateModelForm
    success_url = reverse_lazy('category_list')



