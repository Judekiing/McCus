from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    # created_at = models.DateTimeField(auto_now_add=True)
    # description = models.TextField()


    def __str__(self):
        return self.name[:50]

    def get_absolute_url(self):
        return reverse('blog')



