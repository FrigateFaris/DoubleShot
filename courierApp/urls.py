from django.urls import path

from clientApp.views import OrderDetailPageView
from sellerApp.views import OrdersListPageView, OrderSellerDetailPageView
from .views import *


urlpatterns = [
    path('', OrdersListPageView.as_view(), name='courier_orders'),
    path('<slug:slug>/', OrderSellerDetailPageView.as_view(), name='courier_order_detail'),
    path('/current-courier-orders/', CourierOrdersPageView.as_view(), name='current_courier_orders'),
    path('order/<slug:slug>/', order_accepted, name='accepted'),
    path('order/delivered/<slug:slug>/', order_delivered, name='delivered')
]
