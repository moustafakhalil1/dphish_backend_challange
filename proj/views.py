from django.shortcuts import redirect, render
from .forms import IPAddressForm
from django.http import HttpResponse
from .tasks import process_ip
from django.contrib import messages

# Create your views here.
def submit_ips(request):
    context={}
    if request.method == 'POST':
        form = IPAddressForm(request.POST)
        if form.is_valid():
            ip_addresses = form.cleaned_data['ip_address']
            results = {}
            for ip in ip_addresses:
                result = process_ip.delay(ip.strip())
                
                results[ip.strip()] = result

            for ip, result in results.items():
                task_result = result.get()
                results[ip] = task_result
            print(result)
            context = {
                'form': form,
                'ip_results': results,
            }
        else:
            messages.error(request,'Please Enter Valid Ips')
            return redirect('/')
    else:
        form = IPAddressForm()
        context = {
            'form': form
        }
    return render(request, 'submit_ips.html',context)
   
