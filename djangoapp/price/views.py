from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from price.models import pi_db
from price.serializers import pi_dbSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http.response import Http404, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
import json



#Function that retrieves data from the database and makes it available in the API.
@api_view(['GET'])
def pi_db_list(request):
    list = pi_db.objects.filter(currency="USD-BRL").order_by('-id')
    serializer = pi_dbSerializer(list, many=True)
    return Response(serializer.data)

#Function that displays the main page.
def index(request):
    if request.method == "GET":
        prices = {'prices': pi_db.objects.filter(currency="USD-BRL").order_by('-id')}
        return render(request, 'index.html', prices, )
    if request.method == "POST":
        choose = request.POST.get('currency')
        prices = { 'prices': pi_db.objects.filter(currency=f"{choose}").order_by('-id')}
        return render(request, 'index.html', prices)

  

       
#api_prices        
def prices(request):
        price = pi_db.objects.filter(currency="USD-BRL").order_by('-id')[:10]
        serialied_data = serialize("json", price)
        serialied_data = json.loads(serialied_data)
        return JsonResponse( {'serialied_data': serialied_data})







 
    
    
    
  

    
    











    
    
