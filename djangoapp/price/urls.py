from django.urls import path
from price.views import index

app_name = 'price'
urlpatterns = [
    path('', index, name='index'),
]

