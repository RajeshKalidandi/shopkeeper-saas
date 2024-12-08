from rest_framework import serializers
from .models import Category, Product, Stock

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    current_stock = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'category', 'category_name',
            'sku', 'barcode', 'price', 'cost_price', 'current_stock',
            'minimum_stock', 'maximum_stock', 'created_at', 'updated_at'
        ]

class StockSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = Stock
        fields = [
            'id', 'product', 'product_name', 'transaction_type',
            'quantity', 'reference_number', 'notes', 'created_at'
        ]
        read_only_fields = ['created_at']

    def validate_quantity(self, value):
        if value == 0:
            raise serializers.ValidationError("Quantity cannot be zero.")
        return value
