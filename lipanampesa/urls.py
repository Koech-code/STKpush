from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    lipa_na_mpesa_online
)

urlpatterns = [
    path('lipa-na-mpesa/', lipa_na_mpesa_online, name='lipa_na_mpesa_online'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
                document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
                document_root=settings.MEDIA_ROOT)