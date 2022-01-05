from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('handle-cart',views.handle_cart)
]