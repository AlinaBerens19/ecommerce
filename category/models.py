from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=100, blank=True)
    categort_image = models.ImageField(upload_to='photos/categories', blank=True)
    is_display = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return self.object.get_url()

    def __str__(self):
        return self.category_name
