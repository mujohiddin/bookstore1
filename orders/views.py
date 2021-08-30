from django.views.generic.base import TemplateView
from django.contrib.auth.models import Permission


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'
