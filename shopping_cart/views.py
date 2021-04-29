from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from shopping_cart.cart import Cart
from shopping_cart.models import OrderModel
from store.models import Product


def cart_summary(request):
    cart = Cart(request)
    return render(request, 'shopping_cart/cart_summary.html', {'cart': cart})


@login_required
def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)
        cartqty = cart.__len__()

        response = JsonResponse({'qty': cartqty})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)
        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        cart.update(product=product_id, qty=product_qty)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})
        return response


class OrderHistory(ListView):
    model = OrderModel
    template_name = 'shopping_cart/orderhistory.html'
    context_object_name = 'orders'
    queryset = OrderModel.objects.all()


def submit_order(request):
    OrderModel.objects.create(user=request.user, items=request.session.get('skey'))
    return HttpResponseRedirect(reverse('cart:cart_summary'))








