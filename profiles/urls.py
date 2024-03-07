from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile_view, name='profile_view'),
    path('order_history/<order_id>', views.order_history,
         name='order_history'),
]
