from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ShopProfile

class ShopProfileInline(admin.StackedInline):
    model = ShopProfile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'shop_name', 'phone', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'subscription_status')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Shop info', {'fields': ('shop_name', 'address')}),
        ('Subscription', {'fields': ('subscription_status', 'subscription_end_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'shop_name', 'phone')
    ordering = ('email',)
    inlines = [ShopProfileInline]

@admin.register(ShopProfile)
class ShopProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'business_type', 'gstin')
    search_fields = ('user__email', 'user__shop_name', 'gstin')

admin.site.register(CustomUser, CustomUserAdmin)
