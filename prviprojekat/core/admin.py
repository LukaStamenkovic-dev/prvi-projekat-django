from django.contrib import admin
from .models import Product, Category, ProductImage
from django.utils.html import format_html

# MOZDA CE ZATREBATI
#class ProductImageInline(admin.TabularInline):
    #model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    # MOZDA CE ZATREBATI
    # inlines = [ProductImageInline]

    list_display = ['id', 'title', 'price', 'in_stock', 'image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" />', obj.image.url)
        return "Nema slike"

    def in_stock(self, obj):
        return "Yes" if obj.amount else "No"


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImage)