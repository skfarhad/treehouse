from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('', include('apps.website.urls')),
    path('admin/', admin.site.urls),
    # path('user/', include('apps.user.urls')),
    # path('blog/', include('apps.blog.urls')),
    path('website/', include('apps.website.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Treehouse Admin"
admin.site.site_title = "Treehouse Admin Portal"
admin.site.index_title = "Welcome to Farhad's Admin Portal"
