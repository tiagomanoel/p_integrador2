from django.urls import path, include
from price.views import index
from price.views import pi_db_list



app_name = 'price'
urlpatterns = [
    path('', index, name='index'),
    path('api/', pi_db_list),
]