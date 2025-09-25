from django.contrib import admin   # 👈 you forgot this import
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Smart Waste Management API is running"})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),   # now admin is defined
    path('api/users/', include('users.urls')),
]
