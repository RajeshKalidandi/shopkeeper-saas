from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db import models
from .models import Category, Product, Stock
from .serializers import CategorySerializer, ProductSerializer, StockSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'price', 'quantity']
    search_fields = ['name', 'description', 'sku', 'barcode']
    ordering_fields = ['name', 'price', 'quantity', 'created_at']

    @action(detail=True, methods=['get'])
    def stock_history(self, request, pk=None):
        product = self.get_object()
        stock_entries = Stock.objects.filter(product=product)
        serializer = StockSerializer(stock_entries, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        products = Product.objects.filter(quantity__lte=models.F('reorder_level'))
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['product', 'transaction_type']
    ordering_fields = ['created_at', 'quantity', 'unit_price']

    def perform_create(self, serializer):
        stock = serializer.save()
        product = stock.product
        
        if stock.transaction_type == 'IN':
            product.quantity += stock.quantity
        else:
            product.quantity -= stock.quantity
        product.save()
