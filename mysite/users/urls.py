from django.conf.urls import url

from . import views

urlpatterns = [ url(r'^$', views.index, name='index'),
               	url(r'^courses/$', views.course, name='course'),
               	url(r'^apply/$', views.personaldetails, name='apply')]
