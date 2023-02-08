from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    items = Product.objects.all()
    context = {"items": items}
    return render(request, "shop/home.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {"items": items}
    return render(request, "shop/cart.html", context)


def checkout(request):
    context = {}
    return render(request, "shop/checkout.html", context)


def details(request, pk):
    item = Product.objects.get(pk=pk)
    context = {
        "item": item,
    }
    return render(request, "shop/details.html", context)
