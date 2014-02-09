from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Order index.')

def detail(request, day_id):
    return HttpResponse("You're looking at Day %s." % day_id)

def orders(request, day_id):
    return HttpResponse("You're looking at the order summary of Day %s." % day_id)

def order(request, day_id):
    return HttpResponse("You're ordering for day %s" % day_id)
