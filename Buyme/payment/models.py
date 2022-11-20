from django.db import models


class Item(models.Model):

    CURRENCY_CHOICES = [
        ('usd', 'Dollars'),
        ('try', 'Liras'),
    ]

    name = models.CharField(max_length=64, verbose_name='Имя')
    description = models.TextField(max_length=256, blank=True, verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='usd')

    def __str__(self):
        return self.name

    def get_price(self):
        if self.currency == 'usd':
            return "{0:.2f}".format(self.price / 100)
        else:
            return self.price

