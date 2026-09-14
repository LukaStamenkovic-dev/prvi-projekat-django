from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.shortcuts import render
from ..models import Product

def user(request, user_id):
    return HttpResponse(f"This is user id: {user_id}")