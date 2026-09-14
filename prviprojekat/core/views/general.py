from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.shortcuts import render
from ..models import Product

def home(request):
    # kako zna sta je products odnosno sta je context products
    context = {'products': Product.objects.order_by('-id')[:5]}
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse('Internal Server Error', status = 500)