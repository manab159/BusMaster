from django.shortcuts import render
from wallet.models import Wallet
# Create your views here.

def test_view(request):
    all_cust=Wallet.objects.all()
    specific_cust=Wallet.objects.filter()
