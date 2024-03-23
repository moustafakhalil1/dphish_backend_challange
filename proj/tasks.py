from celery import shared_task
import requests

@shared_task
def process_ip(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    ip_info = response.json()
    return ip_info