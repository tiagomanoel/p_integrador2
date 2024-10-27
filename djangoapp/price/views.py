# Import necessary modules and classes from Django and DRF
from django.shortcuts import render
from rest_framework.decorators import api_view
from price.models import pi_db
from price.serializers import pi_dbSerializer
from rest_framework.response import Response

# Function that retrieves data from the database and makes it available in the API.
from rest_framework.decorators import api_view
from price.models import pi_db
from price.serializers import pi_dbSerializer
from rest_framework.response import Response

@api_view(['GET'])  # Allows only GET requests for this view
def pi_db_list(request):
    # Get the 'currency' parameter from the query string; defaults to None if not present
    currency = request.GET.get('currency', None)

    if currency:
        # If a currency parameter is provided, filter records by currency and return only the most recent one
        record = pi_db.objects.filter(currency=currency).order_by('-id').first()
        records = [record] if record else []  # Create a list only if the record exists
    else:
        # If no parameter is provided, return all records, limited to 38
        records = pi_db.objects.all().order_by('-id')[:38]

    # Serialize the list of records to convert them into a suitable format for the API response
    serializer = pi_dbSerializer(records, many=True)
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
