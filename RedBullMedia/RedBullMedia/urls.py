from django.contrib import admin
from django.urls import path

#Custom URLs

from website.views import MediaContent, ListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListView),
    path('detailedView',MediaContent)
]
