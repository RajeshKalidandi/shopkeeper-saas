from django.urls import path
from . import views

urlpatterns = [
    path('csrf/', views.GetCSRFToken.as_view(), name='csrf_token'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user/', views.UserView.as_view(), name='user'),
]