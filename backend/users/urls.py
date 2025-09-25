from django.urls import path
from .views import RegisterView, UserView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import profile_view

    
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserView.as_view(), name='user'),
    path('profile/', profile_view, name='profile'),
]
