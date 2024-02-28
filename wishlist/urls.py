from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist_view, name='wishlist_viw'),
    path('add_wish/<item_id>/', views.add_product_to_wishlist, name='add_product_to_wishlist'),
]
