# thesis_search_app/urls.py

from django.contrib import admin
from django.urls import path, include  # Include the include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('thesis/', include('thesis.urls')),  # Use include to include the URLs from the thesis app
]
