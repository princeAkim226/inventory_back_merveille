
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_control.urls')),
    path('app/', include('app_control.urls')),
]

urlpatterns +=staticfiles_urlpatterns()