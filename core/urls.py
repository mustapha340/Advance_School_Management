from django.contrib import admin
from django.urls import path, include  # Tumeongeza 'include' hapa

urlpatterns = [
    path('admin/', admin.site.split if hasattr(admin.site, 'split') else admin.site.urls),
    
    # Kuunganisha URL zote za app ya sch kwenye mradi mkuu
    path('', include('sch.urls')),
]