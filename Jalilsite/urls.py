from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include('payment.urls')),
    path('', include('mainapp.urls')),
    path('cgi-sys/defaultwebpage.cgi', RedirectView.as_view(url='', permanent=True))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
