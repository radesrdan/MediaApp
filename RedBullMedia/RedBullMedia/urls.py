from django.contrib import admin
from django.urls import path

#Custom URLs

from website.views import MediaContent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MediaContent),
]
