from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from store import views
from ecommerce import settings

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('accounts/', include('accounts.urls'))
]

urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)