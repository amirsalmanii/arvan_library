import os
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from dotenv import load_dotenv
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

load_dotenv()

try:
    mode = eval(os.environ.get("MODE_PRODUCTION"))
except:
    mode = False

if mode:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/v1/', include(('arvan_lib.api.urls', 'api'))),
    ]
else:
    urlpatterns = [
        path("schema/", SpectacularAPIView.as_view(api_version="v1"), name="schema"),
        path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
        path('admin/', admin.site.urls),
        path('api/v1/', include(('arvan_lib.api.urls', 'api'))),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


