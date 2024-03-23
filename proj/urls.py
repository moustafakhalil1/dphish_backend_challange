
from django.urls import path
from .views import submit_ips
urlpatterns = [
    path('',submit_ips,name='ip_submit'),
]
