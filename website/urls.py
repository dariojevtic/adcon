
from django.conf.urls import include, url
from django.contrib import admin





urlpatterns = [
    url(r'^gallery/', include('gallery.urls')),
    url(r'^admin/', admin.site.urls),
]
