from django.contrib.auth import login, logout
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

from .models import ShopProfile
from .serializers import (
    CustomUserSerializer,
    ShopProfileSerializer,
    UserRegistrationSerializer
)

# Create your views here.

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return Response({'detail': 'CSRF cookie set'})

@method_decorator(csrf_protect, name='dispatch')
class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'user': CustomUserSerializer(user).data,
                'message': 'User Created Successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if username is None or password is None:
            return Response({
                'error': 'Please provide both username and password'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        from django.contrib.auth import authenticate
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return Response({
                'user': CustomUserSerializer(user).data,
                'message': 'Logged in Successfully'
            })
        return Response({
            'error': 'Invalid Credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        logout(request)
        return Response({'message': 'Successfully Logged out'})

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'register':
            return [AllowAny()]
        return super().get_permissions()

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Extract shop_name from validated data
            shop_name = serializer.validated_data.pop('shop_name')
            # Remove confirm_password as we don't need it for user creation
            serializer.validated_data.pop('confirm_password')
            
            # Create user
            user = get_user_model().objects.create_user(
                **serializer.validated_data
            )
            
            # Create associated shop profile
            ShopProfile.objects.create(
                user=user,
                shop_name=shop_name
            )
            
            return Response({
                'user': CustomUserSerializer(user).data,
                'message': 'Registration successful'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShopProfileViewSet(viewsets.ModelViewSet):
    queryset = ShopProfile.objects.all()
    serializer_class = ShopProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_staff:
            return ShopProfile.objects.filter(user=self.request.user)
        return ShopProfile.objects.all()
