from ..models import Product
from django.shortcuts import render, redirect

def add_to_cart(request, product_id):

    cart = request.session.get("shopping_cart", {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session["shopping_cart"] = cart
    request.session.modified = True


    return redirect("cart_details")

def show_cart(request):

    cart = request.session.get("shopping_cart", {})

    items = []
    total_cart = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=int(product_id))

        total_price_for_product = product.current_price * quantity
        total_cart += total_price_for_product

        items.append({
            'product': product,
            'quantity': quantity,
            'total_price': total_price_for_product
        })

    return render(request, "shopping_cart.html", {
        "items": items,
        "total_cart": total_cart
    })

def remove_from_cart(request, product_id):
    cart = request.session.get("shopping_cart", {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session["shopping_cart"] = cart
    request.session.modified = True

    return redirect("cart_details")