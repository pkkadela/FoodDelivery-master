from django.urls import path

from . import views

urlpatterns = [
    path('', views.CheckDetails.as_view(), name='payment-home'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/',views.success),
    path('cancelled/', views.CancelledView.as_view()),
]