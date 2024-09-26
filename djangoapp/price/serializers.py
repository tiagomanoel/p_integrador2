from price.models import pi_db
from rest_framework import serializers


class pi_dbSerializer(serializers.ModelSerializer):
    class Meta:
        model = pi_db
        fields = ['id', 'date', 'value', 'currency']