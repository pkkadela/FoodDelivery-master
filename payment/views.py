from django.shortcuts import render
from django.conf import settings
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from django.views.generic.base import TemplateView
import stripe

class CheckDetails(TemplateView):
    template_name = 'payment/payment.html'

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/payment/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'Food',
                        'quantity': 1,
                        'currency': 'inr',
                        'amount': request.user.cart.total_price*100,
                    }
                ],
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            print('exceptions', e)
            return JsonResponse({'error': str(e)})

def success(request):
    for food in request.user.cart.food_set.all():
        food.delete()
    request.user.cart.total_price = 0
    request.user.cart.save()
    return render(request, 'payment/success.html')


class CancelledView(TemplateView):
    template_name = 'payment/cancelled.html'