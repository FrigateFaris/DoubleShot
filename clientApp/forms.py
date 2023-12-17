from django import forms
from django.contrib.auth.forms import AuthenticationForm

from clientApp.models import Client, Order


class ClientRegistrationModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('username', 'email', 'password', 'delivery_address')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control'})
        }
        help_texts = {
            'username': ''
        }


class ProfileToUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('username', 'email', 'delivery_address')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control'})
        }
        help_texts = {
            'username': ''
        }


class ClientLoginModelForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('phone_number', 'delivery_address', 'discount_coupon')
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control'}),
            'discount_coupon': forms.PasswordInput(attrs={'class': 'form-control'})
        }
