from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('app_library.urls')),
    path('users/', include('app_user.urls')),
]
