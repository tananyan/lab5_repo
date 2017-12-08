from django.conf.urls import url, include

from myapp.views import OrdersView, OrderView
from . import views

urlpatterns = [
    url(r'^orders/', OrdersView.as_view(), name="orders"),
    url(r'^order/(?P<id>\d+)', OrderView.as_view(), name='order_url')
    #url(r'^ExampleClassBased/', ExampleClassBased.as_view()),
]
