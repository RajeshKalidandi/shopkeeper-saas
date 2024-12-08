from django.contrib import admin
from .models import Category, Product, Stock

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'sku', 'price', 'quantity')
    list_filter = ('category',)
    search_fields = ('name', 'sku', 'barcode')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'transaction_type', 'quantity', 'created_at')
    list_filter = ('transaction_type', 'created_at')
    search_fields = ('product__name', 'reference_number')
