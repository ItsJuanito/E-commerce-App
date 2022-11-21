from django.shortcuts import render, redirect

from .cart import Cart

# Create your views here.
def cart_detail(request):
    cart = Cart(request)
    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)

        return redirect('cart')

    if change_quantity:
        cart.add(change_quantity, quantity, True)

        return redirect('cart')

    return render(request, 'cart/cart.html')

def success_page(request):
    cart = Cart(request)
    cart.clear()
    
    return render(request, 'cart/success_page.html')