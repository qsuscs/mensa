from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from order.models import Day

def index(request):
    this_week_list = Day.objects.all().order_by('-date')[:5]
    template = loader.get_template('orders/index.html')
    context = RequestContext(request, {
        'this_week_list': this_week_list,
    })
    return HttpResponse(template.render(context))

def detail(request, day_id):
    try:
        day = Day.objects.get(pk=day_id)
    except Day.DoesNotExist:
        raise Http404
    return render(request, 'orders/detail.html', {'day': day})

def orders(request, day_id):
    return HttpResponse("You're looking at the order summary of Day %s." % day_id)

def order(request, day_id):
    return HttpResponse("You're ordering for day %s" % day_id)
