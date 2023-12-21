from django.urls import path

from .views import *


urlpatterns = [
    path('category-list/', AlcoholCategoryListPageView.as_view(), name='category_list'),
    path('category-list/<slug:slug>/', AlcoholCategoryDetailPageView.as_view(), name='category_detail'),
    path('category-list/<slug:slug>/', AlcoholCategoryDetailPageView.as_view(), name='category_detail_paginated'),
    path('category-list/product/<slug:slug>/', ProductDetailPageView.as_view(), name='product_detail'),
    path('category-list/product/delete/<slug:slug>/', DeleteProductPageView.as_view(), name='product_delete'),
    path('category-list/product/update/<slug:slug>/', UpdateProductPageView.as_view(), name='update_product'),
    path('category-list/product/update/update-successfully/', SuccessUpdatingPageView.as_view(), name='success_updating'),
    path('create-product/', CreateProductPageView.as_view(), name='create_product'),
    path('orders-list/', OrdersListPageView.as_view(), name='orders_list'),
    path('orders-list/<slug:slug>/', OrderSellerDetailPageView.as_view(), name='seller_order_detail'),
    path('orders-list/product/approved/<slug:slug>/', order_approved_status, name='approved'),
    path('orders-list/product/denied/<slug:slug>/', order_denied_status, name='denied'),
    path('create-category/', CategoryCreatePageView.as_view(), name='create_category'),
    path('create-brand/', BrandCreatePageView.as_view(), name='create_brand'),
]
