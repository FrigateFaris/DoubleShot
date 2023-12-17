from django import forms

from clientApp.models import Order
from sellerApp.models import Product


class UpdateProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('slug', 'rating')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'volume': forms.NumberInput(attrs={'class': 'form-control'}),
            'alcohol_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CreateProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('slug', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'volume': forms.NumberInput(attrs={'class': 'form-control'}),
            'alcohol_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class OrderSellerModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'phone_number', 'delivery_address', 'discount_coupon', 'order_date', 'total_price')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control'}),
            'discount_coupon': forms.TextInput(attrs={'class': 'form-control'}),
            'order_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
