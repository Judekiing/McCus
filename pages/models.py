from django.conf import settings 
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    store_name = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    category = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    description = models.TextField()


    def __str__(self):
        return self.product_name[:50]

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=140)
    # rating = 
    username = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    email = models.CharField(max_length=140)
    # profile_pic = 
    date = models.DateTimeField(auto_now_add=True)


