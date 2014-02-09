from django.conf.urls import patterns, url

from order import views

urlpatterns = patterns('',
    # ex: /order/
    url(r'^$', views.index, name='index'),
    # ex: /order/42/
    url(r'^(?P<day_id>\d+)/$', views.detail, name='detail'),
    # ex: order/42/orders/
    url(r'^(?P<day_id>\d+)/orders/$', views.orders, name='orders'),
    # ex: /order/42/order/
    url(r'^(?P<day_id>\d+)/order/$', views.order, name='order'),
)
