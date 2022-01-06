from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('mainapp.urls', 'home'), namespace='home')),
    path('announcements/', include('mainapp.urls')),
    path('eteacher/', include('mainapp.urls')),
    path('estudent/', include('mainapp.urls')),
    path('announcements-list/', include('mainapp.urls')),
    path('summernote/', include('django_summernote.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
