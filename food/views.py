from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    context = {
        'foods': Food.objects.all(),
    }
    if request.user.is_authenticated:
        context['cart'] = Food.objects.filter(cart=request.user.cart)
    return render(request, 'food/mainpage.html', context)

@login_required
def handle_cart(request):
    if request.method == 'POST':
        if request.POST.get('add_to_cart'):
            food = Food.objects.get(index = request.POST.get('add_to_cart') )
            request.user.cart.food_set.add(food)
            request.user.cart.total_price = request.user.cart.total_price + food.price
        elif request.POST.get('remove_from_cart'):
            food = Food.objects.get(index = request.POST.get('remove_from_cart') )
            request.user.cart.food_set.remove(food)
            request.user.cart.total_price = request.user.cart.total_price - food.price
    request.user.save()
    return redirect('home')