from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls, name='admin'),
	path('', include(('core.urls', 'core'), namespace='core')),
	path('app/', include(('app.urls', 'app'), namespace='app')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)