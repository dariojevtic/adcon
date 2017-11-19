from django.conf.urls import url

from . import views

urlpatterns = [
               # ex: /gallery/
               url(r'^$', views.index, name='gallery'),
]
