from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, DetailsForm
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.contrib.auth import views as auth_views

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, message=f'Account created for {username}! Please login to continue...')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def cart(request):
    if request.method =='POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            new_detail = form.save(commit=False)
            new_detail.cart = request.user.cart
            new_detail.save()
            return redirect('payment-home')
    else:
        form = DetailsForm()
    return render(request, 'user/cart.html', {'form': form})

@login_required
def empty_cart(request):
    for food in request.user.cart.food_set.all():
        food.cart = None
        food.save()
    request.user.cart.total_price = 0
    request.user.cart.save()
    return redirect('home')