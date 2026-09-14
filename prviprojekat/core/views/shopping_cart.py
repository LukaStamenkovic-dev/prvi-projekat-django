from ..models import Product, Order, OrderItem
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_page')
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

@login_required(login_url='login_page')
def show_order_form(request):
    return render(request, 'order_form.html')

@login_required(login_url='login_page')
def finish_order(request):
    cart = request.session.get('shopping_cart', {})

    if not cart or request.method != 'POST':
        return redirect('cart_details')

    full_name = request.POST.get('full_name')
    country = request.POST.get('country')
    city = request.POST.get('city')
    postal_code = request.POST.get('postal_code')
    phone = request.POST.get('phone')

    order = Order.objects.create(
        user=request.user,
        full_name=full_name,
        country=country,
        city=city,
        postal_code=postal_code,
        phone=phone
    )

    for product_id, quantity in cart.items():

        product = Product.objects.get(id=int(product_id))

        OrderItem.objects.create(
            order=order,
            product_id=product_id,
            quantity=quantity,
            price=quantity * product.current_price
        )

    request.session['cart'] = {}
    
    return redirect('home_page')

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

@login_required(login_url='login_page')
def remove_from_cart(request, product_id):
    cart = request.session.get("shopping_cart", {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session["shopping_cart"] = cart
    request.session.modified = True

    return redirect("cart_details")

