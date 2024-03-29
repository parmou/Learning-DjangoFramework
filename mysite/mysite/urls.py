from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    path('register/', include('Profile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
