# Import the pi_db model from the price application
from price.models import pi_db
# Import the serializers module from Django REST framework
from rest_framework import serializers

# Define a serializer class for the pi_db model
class pi_dbSerializer(serializers.ModelSerializer):
    # Define the Meta class to specify model and fields for serialization
    class Meta:
        # Specify the model to be serialized
        model = pi_db
        # Specify the fields to be included in the serialized output
        fields = ['id', 'date', 'value', 'currency']
