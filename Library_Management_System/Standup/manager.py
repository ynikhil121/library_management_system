from django.db import models


class CustomManager(models.Manager):
    def all_book_in_desc_price(request):
        return super().order_by('-Price')

    def all_book_in_asce_price(request):
        return super().order_by('Price')

    def all_book_in_category(request):
        return super().filter('')
