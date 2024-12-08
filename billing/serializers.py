from rest_framework import serializers
from .models import Invoice, InvoiceItem, Payment

class InvoiceItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = InvoiceItem
        fields = [
            'id', 'product', 'product_name', 'quantity',
            'unit_price', 'discount', 'tax_rate', 'total'
        ]

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True)
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    
    class Meta:
        model = Invoice
        fields = [
            'id', 'invoice_number', 'customer', 'customer_name',
            'date', 'due_date', 'items', 'subtotal', 'tax_total',
            'discount_total', 'grand_total', 'status', 'notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['invoice_number', 'created_at', 'updated_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)
        
        for item_data in items_data:
            InvoiceItem.objects.create(invoice=invoice, **item_data)
        
        return invoice

class PaymentSerializer(serializers.ModelSerializer):
    invoice_number = serializers.CharField(source='invoice.invoice_number', read_only=True)
    
    class Meta:
        model = Payment
        fields = [
            'id', 'invoice', 'invoice_number', 'amount',
            'payment_method', 'reference_number', 'notes',
            'payment_date', 'created_at'
        ]
        read_only_fields = ['created_at']
