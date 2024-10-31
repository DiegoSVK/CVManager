
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('auth/plataforma/formularios/', include('app_forms.urls')),
    path('auth/plataforma/',include('cv_platform.urls'))
]
