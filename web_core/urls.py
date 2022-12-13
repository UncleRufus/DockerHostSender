# Imports
from django.contrib import admin
from django.urls import path

# Routers
from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls