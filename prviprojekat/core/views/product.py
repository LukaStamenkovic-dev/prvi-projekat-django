from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.shortcuts import render
from ..models import Product
from django.contrib.auth.decorators import login_required

def product(request, name):

    try:
        product = Product.objects.get(title=name)
    except Product.DoesNotExist:
        return HttpResponseNotFound(f"Product {name} not available")
    
    # pitaj za context:{'product': product}
    context = {'product': product}

    return render(request, 'product.html', context)

