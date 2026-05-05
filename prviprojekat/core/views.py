from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('Internal Server Error', status = 500)

def products(request, name):
    return HttpResponse(f"This is {name}")

def user(request, user_id):
    return HttpResponse(f"This is user id: {user_id}")