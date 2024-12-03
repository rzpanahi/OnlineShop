from django.urls import path
from .views import index, store

urlpatterns = [
    path('index/', index, name='index'),
    path('store/', store, name='store'),
]