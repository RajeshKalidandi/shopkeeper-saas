"""
URL configuration for shopkeeper_pro project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to ShopKeeper Pro API",
        "version": "1.0",
        "documentation": {
            "api_root": "/api/v1/",
            "admin": "/admin/"
        }
    })

# Import ViewSets
from accounts.views import CustomUserViewSet, ShopProfileViewSet
from inventory.views import CategoryViewSet, ProductViewSet, StockViewSet
from billing.views import InvoiceViewSet, PaymentViewSet
from crm.views import CustomerViewSet, CustomerInteractionViewSet, LoyaltyViewSet

# Create a router and register our viewsets
router = routers.DefaultRouter()

# Accounts URLs
router.register(r'users', CustomUserViewSet)
router.register(r'shops', ShopProfileViewSet)

# Inventory URLs
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'stock', StockViewSet)

# Billing URLs
router.register(r'invoices', InvoiceViewSet)
router.register(r'payments', PaymentViewSet)

# CRM URLs
router.register(r'customers', CustomerViewSet)
router.register(r'interactions', CustomerInteractionViewSet)
router.register(r'loyalty', LoyaltyViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('accounts.urls')),  # Add this line for authentication endpoints
    path('api-auth/', include('rest_framework.urls')),
]

# Serve media files in development
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
