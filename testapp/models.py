from django.db import models
class Product(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length = 100)
    image = models.URLField()
    rating=models.DecimalField(max_digits=5,decimal_places=1)
