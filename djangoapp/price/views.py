from django.shortcuts import render
from rest_framework.decorators import api_view
from price.models import pi_db
from price.serializers import pi_dbSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

#Function that retrieves data from the database and makes it available in the API.
@api_view(['GET'])
def pi_db_list(request):
    list = pi_db.objects.all().order_by('-id').values()[:62]
    serializer = pi_dbSerializer(list, many=True)
    return Response(serializer.data)

#Function that displays the main page.
def index(request):
    prices = {
        'prices': pi_db.objects.all()
    }    
    return render(request, 'index.html', prices)











# def api(request):
#     conn = psycopg2.connect(database = "pi_db", 
#                         user = "pi_user", 
#                         host= '127.0.0.1',
#                         password = "projeto_integrador2",
#                         port = 5432)
    
    
#     cursor = conn.cursor()
#     cursor.execute(f'SELECT * FROM price_pi_db;')
#     rows = cursor.fetchall()
#     conn.commit()
#     conn.close()
#     return render(request, jsonify(rows)) # type: ignore
    
    
