from django.contrib import admin
from django.urls import path
from Dijango_basics.views import hello_geeks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_geeks),  # Match the root URL
]
