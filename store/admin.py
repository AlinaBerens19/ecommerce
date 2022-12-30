from decimal import Decimal

from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "price", "discount", "stock", "is_available", "created_date", "modified_date",
                    "images", "vat", "after_discount")
    prepopulated_fields = {"slug": ("product_name",)}
    list_filter = ("is_available", "created_date")

    def vat(self, obj: Product) -> str:
        return f"{(obj.price * Decimal(0.05)):.2f}$"

    def after_discount(self, obj: Product) -> str:
        return f"{(obj.price - (obj.price * obj.discount/100)):.2f}$"


admin.site.register(Product, ProductAdmin)
