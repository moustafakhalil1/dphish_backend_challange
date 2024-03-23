# forms.py
from django import forms
from .models import IPAddress
from django.core.exceptions import ValidationError

import ipaddress

class IPAddressForm(forms.ModelForm):
    class Meta:
        model = IPAddress
        fields = ['ip_address']
    def clean_ip_address(self):
        ip_addresses = self.cleaned_data['ip_address'].split(',')
        cleaned_ip_addresses = []

        for ip_address in ip_addresses:
            ip_address = ip_address.strip()
            try:
                # Validate the IP address format
                ipaddress.ip_address(ip_address)
                cleaned_ip_addresses.append(ip_address)
            except ValueError:
                # If the IP address is invalid, raise a validation error
                raise ValidationError(f"Invalid IP address format: {ip_address}")

        return cleaned_ip_addresses   