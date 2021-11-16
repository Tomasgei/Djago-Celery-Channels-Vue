from django.urls import path
from .consumers import Coin_BoardConsumer

ws_urlpatterns = [
    path("ws/coins/", Coin_BoardConsumer.as_asgi() )
]