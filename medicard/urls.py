
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import views as auth_view
import allauth



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/login/',include('django.contrib.auth.urls') allauth.account.views.LoginView),
    #  url(r'^accounts/login', include('allauth.urls')),
    
    path('', include('bambi.urls')),    
    # url(r'^accounts/', include('authtools.urls')),
       url(r'^accounts/', include('allauth.urls')),
      path('accounts/', include('django.contrib.auth.urls')),
    
       
       url(r'^rest-auth/', include('rest_auth.urls')),
       path('accounts/password_reset/', auth_view.PasswordResetView.as_view(
        html_email_template_name='registration/password_reset_html_email.html')),

          url(r'^notifications/', include('notify.urls', 'notifications'))
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



