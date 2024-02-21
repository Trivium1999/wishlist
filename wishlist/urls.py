from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from wishlist import settings
# from  import page_not_found


handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/', include('users.urls', namespace='users')),
    # path('auth/', include('django.contrib.auth.urls')),
    path('', include('list.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

# handler404 = 'list.views.page_not_found'
# handler500 = serverError
