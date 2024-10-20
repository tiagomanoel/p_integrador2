from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from price.models import pi_db
from price.serializers import pi_dbSerializer
from rest_framework.response import Response
# from django.http import JsonResponse
from django.core.serializers import serialize
# import json



#Function that retrieves data from the database and makes it available in the API.
@api_view(['GET'])
def pi_db_list(request):
    list = pi_db.objects.filter(currency="USD-BRL").order_by('-id')
    serializer = pi_dbSerializer(list, many=True)
    return Response(serializer.data)


#Function that displays the main page.
def index(request):
    if request.method == "GET":
        prices = {'prices': pi_db.objects.filter(currency="USD-BRL").order_by('id')[:10]}
        return render(request, 'index.html', prices, )
    if request.method == "POST":
        choose = request.POST.get('currency')
        prices = { 'prices': pi_db.objects.filter(currency=f"{choose}").order_by('-id')[:10]}
        return render(request, 'index.html', prices)
    
def pji(request):
    return render(request, 'pji.html') 

def document(request):
    return render(request, 'document.html')
    

 

  

       
# #api_prices        
# def prices(request):
#         price = pi_db.objects.filter(currency="USD-BRL").order_by('-id')[:10]
#         serialied_data = serialize("json", price)
#         serialied_data = json.loads(serialied_data)
#         return JsonResponse( {'serialied_data': serialied_data})







 
    
    
    
  

    
    











    
    
