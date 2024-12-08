from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ShopProfile

CustomUser = get_user_model()

class ShopProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopProfile
        fields = ['id', 'shop_name', 'address', 'phone', 'gst_number', 'subscription_status']

class CustomUserSerializer(serializers.ModelSerializer):
    shop_profile = ShopProfileSerializer(read_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'password', 'shop_profile']
        read_only_fields = ['is_active']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserRegistrationSerializer(serializers.ModelSerializer):
    shop_name = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'confirm_password', 'first_name', 'last_name', 'shop_name']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        shop_name = validated_data.pop('shop_name')
        
        # Create user
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(
            **validated_data,
            is_active=True
        )
        user.set_password(password)
        user.save()

        # Create shop profile
        ShopProfile.objects.create(
            user=user,
            shop_name=shop_name,
            subscription_status='trial'
        )
        
        return user
