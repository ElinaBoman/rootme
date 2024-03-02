from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist_view, name='wishlist_view'),
    path('add_wish/<product_id>/', views.add_product_to_wishlist, name='add_product_to_wishlist'),
     path('delete_wish/<product_id>/', views.delete_product_from_wishlist, name='delete_product_from_wishlist'),  
]
