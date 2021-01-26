
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # User Management
    path('accounts/',include('django.contrib.auth.urls')),
    

    # Local apps
    path('',include('pages.urls')),
    path('accounts/',include('users.urls')),
]
