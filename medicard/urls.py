
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', include('bambi.urls')),    
    # url(r'^accounts/', include('authtools.urls')),
       url(r'^accounts/', include('allauth.urls')),
       url(r'^rest-auth/', include('rest_auth.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
