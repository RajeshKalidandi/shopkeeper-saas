from rest_framework import serializers
from .models import Customer, CustomerInteraction, Loyalty

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id', 'name', 'phone', 'email', 'address',
            'date_of_birth', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

class CustomerInteractionSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    
    class Meta:
        model = CustomerInteraction
        fields = [
            'id', 'customer', 'customer_name', 'interaction_type',
            'notes', 'interaction_date', 'follow_up_date',
            'created_at'
        ]
        read_only_fields = ['created_at']

class LoyaltySerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    
    class Meta:
        model = Loyalty
        fields = [
            'id', 'customer', 'customer_name', 'points',
            'tier', 'last_points_earned', 'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
