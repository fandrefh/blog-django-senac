from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.sobre_nos, name='sobre-nos'),
]