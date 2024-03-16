from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from wishlist import settings
# from core.views import page_not_found, server_error, permission_denied


handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('list.urls', 'wishlist')),
    path('users/', include('users.urls', 'users'))
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
