from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Customer, CustomerInteraction, Loyalty
from .serializers import CustomerSerializer, CustomerInteractionSerializer, LoyaltySerializer

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'phone', 'email']
    search_fields = ['name', 'phone', 'email']
    ordering_fields = ['name', 'created_at']

    @action(detail=True, methods=['get'])
    def interactions(self, request, pk=None):
        customer = self.get_object()
        interactions = CustomerInteraction.objects.filter(customer=customer)
        serializer = CustomerInteractionSerializer(interactions, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def loyalty(self, request, pk=None):
        customer = self.get_object()
        try:
            loyalty = Loyalty.objects.get(customer=customer)
            serializer = LoyaltySerializer(loyalty)
            return Response(serializer.data)
        except Loyalty.DoesNotExist:
            return Response({'detail': 'Loyalty profile not found'}, status=404)

class CustomerInteractionViewSet(viewsets.ModelViewSet):
    queryset = CustomerInteraction.objects.all()
    serializer_class = CustomerInteractionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['customer', 'interaction_type']
    ordering_fields = ['interaction_date', 'follow_up_date']

class LoyaltyViewSet(viewsets.ModelViewSet):
    queryset = Loyalty.objects.all()
    serializer_class = LoyaltySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['customer', 'tier']
    ordering_fields = ['points', 'last_points_earned']
