# Import necessary modules and classes from Django and DRF
from django.shortcuts import render
from rest_framework.decorators import api_view
from price.models import pi_db
from price.serializers import pi_dbSerializer
from rest_framework.response import Response

# Function that retrieves data from the database and makes it available in the API.
@api_view(['GET'])  # Allows only GET requests for this view
def pi_db_list(request):
    # Query the database for records with the currency "USD-BRL" and order them by descending ID
    list = pi_db.objects.filter(currency="USD-BRL").order_by('-id')
    # Serialize the list of records to convert them into a format suitable for the API response
    serializer = pi_dbSerializer(list, many=True)
    # Return the serialized data as a JSON response
    return Response(serializer.data)

# Function that displays the main page.
def index(request):
    # Handle GET requests to display the main page with the latest 10 prices
    if request.method == "GET":
        # Query the database for the latest 10 records with currency "USD-BRL"
        prices = {'prices': pi_db.objects.filter(currency="USD-BRL").order_by('id')[:10]}
        # Render the 'index.html' template with the retrieved prices
        return render(request, 'index.html', prices)
    
    # Handle POST requests to update the displayed prices based on user selection
    if request.method == "POST":
        # Get the selected currency from the form data
        choose = request.POST.get('currency')
        # Query the database for the latest 10 records matching the selected currency
        prices = {'prices': pi_db.objects.filter(currency=f"{choose}").order_by('-id')[:10]}
        # Render the 'index.html' template with the updated prices
        return render(request, 'index.html', prices)

# Function to render the 'pji.html' page
def pji(request):
    return render(request, 'pji.html') 

# Function to render the 'sobre.html' page
def sobre(request):
    return render(request, 'sobre.html')
