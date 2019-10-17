from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),

]
