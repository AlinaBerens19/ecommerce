from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    # product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    discount = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def after_discount(self):
        return self.price - (self.price * self.discount/100)
