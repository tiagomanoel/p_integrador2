from django.urls import path, include
from price.views import index, prices
from price.views import pi_db_list
from django.conf.urls.static import static
from django.conf import settings



app_name = 'price'
urlpatterns = [
    path('', index, name='index'),
    path('api/', pi_db_list, name='api'),
    path('prices/', prices, name='prices'),

    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)