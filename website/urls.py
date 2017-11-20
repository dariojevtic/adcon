
from django.conf.urls import include, url
from django.contrib import admin
from homepage import views



urlpatterns = [
    url(r'^gallery/', include('gallery.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='homepage'),
]
