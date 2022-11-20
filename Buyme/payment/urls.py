from django.urls import path
from .views import ItemListView, SuccessView, CancelView, MainView, PaymentIntentView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('item/<int:id>', ItemListView.as_view(), name='index'),
    path('buy/<int:id>', PaymentIntentView.as_view(), name='create-payment-intent'),
]