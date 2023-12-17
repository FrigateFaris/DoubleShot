from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(OrderHistory)
# admin.site.register(OrderHistoryItem)
