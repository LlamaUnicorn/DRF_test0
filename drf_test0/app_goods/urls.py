from django.urls import path
from app_goods.views import items_list

urlpatterns = [
    path('items/', items_list, name='items_list'),
]
