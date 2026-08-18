from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.shortcuts import render

products = {
        "Macbook Air 2025": {
            'price': 2000,
            'description': 'This is Macbook Air 2025'
        },
        "iPhone 16 Pro": {
            'price': 1200,
            'description': 'Latest iPhone 16 Pro with advanced camera system'
        },
        "Samsung Galaxy S25": {
            'price': 1100,
            'description': 'Flagship Samsung phone with powerful performance'
        },
        "Dell XPS 15": {
            'price': 1800,
            'description': 'High-performance laptop for professionals'
        },
        "Sony WH-1000XM6": {
            'price': 400,
            'description': 'Noise-cancelling wireless headphones'
        }
    }


def home(request):
    # kako zna sta je products odnosno sta je context products
    context = {'products': products}
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse('Internal Server Error', status = 500)

def product(request, name):
    # kako zna sta je name
    product = products.get(name)
    if not product:
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

    return HttpResponse(f"This is {title}, {price}, {description}", status = 201)