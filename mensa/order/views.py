from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    this_week_list = Day.objects.order_by('-date')[:5]
    template = loader.get_template('orders/index.html')
    context = RequestContext(request, {
        'this_week_list': this_week_list,
    })
    return HttpResponse(template.render(context))

def detail(request, day_id):
    return HttpResponse("You're looking at Day %s." % day_id)

def orders(request, day_id):
    return HttpResponse("You're looking at the order summary of Day %s." % day_id)

def order(request, day_id):
    return HttpResponse("You're ordering for day %s" % day_id)
