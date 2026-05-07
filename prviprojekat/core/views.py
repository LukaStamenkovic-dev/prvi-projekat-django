from django.http import HttpResponse, HttpResponseNotFound
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