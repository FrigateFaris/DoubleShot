from django.urls import path

from sellerApp.views import StartPageView, AlcoholCategoryListPageView, AlcoholCategoryDetailPageView, \
    ProductDetailPageView
from .views import *


urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('registration/', ClientRegistrationPageView.as_view(), name='registration_page'),
    path('logout-request/', ClientLogoutPageView.as_view(), name='logout_request'),
    path('logout-request/logout/', logout_client, name='logout'),
    path('login/', ClientLoginPageView.as_view(), name='login_page'),
    path('category-list/', AlcoholCategoryListPageView.as_view(), name='categories'),
    path('category-list/<slug:slug>/', AlcoholCategoryDetailPageView.as_view(), name='products'),
    path('category-list/product/<slug:slug>/', ProductDetailPageView.as_view(), name='detail_product'),
    path('category-list/add_to_cart_product/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('profile/<int:pk>', ProfilePageView.as_view(), name='profile'),
    path('profile/change-quantity/<int:item_id>/<slug:action>/', change_quantity, name='change_quantity'),
    path('profile/order/', CurrentOrderPageView.as_view(), name='order'),
    path('profile/order/confirmation/', ConfirmationRequestPageView.as_view(), name='confirmation'),
    path('profile/<slug:slug>/', OrderDetailPageView.as_view(), name='order_detail'),
]
