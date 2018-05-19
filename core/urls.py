from django.urls import path
from .views import list_clients, add_client, update_client, delete_client

urlpatterns = [
    path('', list_clients, name="list_clients"),
    path('add/', add_client, name="add_client"),
    path('update/<int:pk>', update_client, name="update_client"),
    path('delete/<int:pk>', delete_client, name="delete_client")
]