from django.shortcuts import render
#import requests
from django.core.paginator import Paginator

# Create your views here.

def IndexView(request):
   # url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    #coins = requests.get(url).json()
   

    #p = Paginator(coins,25)
    #page = request.GET.get("page")
    #coins_data = p.get_page(page)

    #context = {"coins": coins, "coins_data":coins_data }
    context = {}
    return render(request, "index.html", context)
