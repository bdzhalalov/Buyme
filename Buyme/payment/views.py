
import os

import stripe
from django.http import Http404
from rest_framework.views import APIView
from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework.response import Response
from dotenv import load_dotenv

from .serializers import ItemSerializer
from .models import Item

load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


class MainView(TemplateView):
    template_name = 'main.html'

    def get(self, request):
        items = Item.objects.all()
        context = {
            'items': items
        }
        return render(request, self.template_name, context)


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


class ItemListView(APIView):
    template_name = 'item.html'

    def get_object(self, id):
        try:
            return Item.objects.get(pk=id)
        except:
            raise Http404

    def get(self, request, id):
        item = self.get_object(id)
        serializer = ItemSerializer(item)
        context = {
            'id': serializer.data['id'],
            'name': serializer.data['name'],
            'description': serializer.data['description'],
            'price': item.get_price(),
            'currency': serializer.data['currency'],
            'STRIPE_PUBLIC_KEY': os.getenv('STRIPE_PUBLIC_KEY')
        }
        return render(request, self.template_name, context=context)


class PaymentIntentView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            item_id = self.kwargs['id']
            item = Item.objects.get(pk=item_id)
            if item.currency == 'usd':
                amount = item.price
            else:
                amount = item.get_price() * 100
            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=item.currency,
                automatic_payment_methods={
                    'enabled': True,
                },
            )
            return Response({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return Response({'error': str(e)})
