from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, viewsets
from django.conf.urls.static import static

from core import settings
from mainapp.views import TestSuiteViewSet, InputImageViewSet, StandardImageViewSet

router = routers.DefaultRouter()
router.register(r'test_suite', TestSuiteViewSet)
router.register(r'std_image', StandardImageViewSet)
router.register(r'input_image', InputImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(('mainapp.urls', 'mainapp'), namespace="mainapp")),
    url(r'^api/upload/', include(router.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
