from django.urls import path
from .views import index, store, product, checkout

urlpatterns = [
    path('index/', index, name='index'),
    path('store/', store, name='store'),
    path('product/', product, name='product'),
    path('checkout/', checkout, name='checkout'),
]