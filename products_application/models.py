from django.db import models

# Create your models here.
class Product (models.Model):
  name = models.CharField(max_length=80)
  quantity = models.IntegerField(default=0)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  image = models.ImageField(upload_to='products_application/uploads')
