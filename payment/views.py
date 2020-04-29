from django.shortcuts import render, redirect
from django.http import HttpResponse
from pypaystack import Transaction, Customer, Plan
from django.conf import settings

# Create your views here.
def charge(request):
    return render(request, 'payment/checkout.html')

def verify(request, reference):
    transaction = Transaction(settings.SK_KEY)
    response = transaction.verify(reference)
    if response[3]['status'] == 'success':
        return render(request,'pages/success.html')
    else:
        return HttpResponse('failed')
    # return HttpResponse(response)