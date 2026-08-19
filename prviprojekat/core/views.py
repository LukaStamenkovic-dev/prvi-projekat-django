from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.shortcuts import render
from .models import Product


def home(request):
    # kako zna sta je products odnosno sta je context products
    context = {'products': Product.objects.order_by('-id')[:5]}
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse('Internal Server Error', status = 500)

def product(request, name):

    try:
        product = Product.objects.get(title=name)
    except Product.DoesNotExist:
        return HttpResponseNotFound(f"Product {name} not available")

    context = {'product': product}

    return render(request, 'product.html', context)
    

def user(request, user_id):
    return HttpResponse(f"This is user id: {user_id}")

def create_product(request):
    return render(request, "product_create.html")

def save_product(request):

    if request.method != "POST":
        return HttpResponseNotAllowed("This method is not allowed.")

    title = request.POST.get('title')
    price = request.POST.get('price')
    description = request.POST.get('description')

    if not title or not price or not description:
        return HttpResponse("All fields are required", status = 400)

    product = Product(title=title, price=price, description=description)
    product.save()

    return HttpResponse(f"This is {title}, {price}, {description}", status = 201)