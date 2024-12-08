from django.contrib import admin
from .models import Customer, CustomerInteraction, Loyalty

class CustomerInteractionInline(admin.TabularInline):
    model = CustomerInteraction
    extra = 1

class LoyaltyInline(admin.TabularInline):
    model = Loyalty
    extra = 0
    max_num = 1

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    search_fields = ('name', 'phone', 'email')
    inlines = [LoyaltyInline, CustomerInteractionInline]
    readonly_fields = ('created_at', 'updated_at')

@admin.register(CustomerInteraction)
class CustomerInteractionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'interaction_type', 'interaction_date', 'follow_up_date')
    list_filter = ('interaction_type', 'interaction_date')
    search_fields = ('customer__name', 'notes')

@admin.register(Loyalty)
class LoyaltyAdmin(admin.ModelAdmin):
    list_display = ('customer', 'points', 'tier', 'last_points_earned')
    list_filter = ('tier',)
    search_fields = ('customer__name',)
