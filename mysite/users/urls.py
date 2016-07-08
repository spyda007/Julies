from django.conf.urls import url

from . import views

urlpatterns = [ url(r'^$', views.index, name='index'),
               	url(r'^courses/$', views.course, name='course'),
               	url(r'^login/apply/$', views.personaldetails, name='apply'),
               	url(r'^login/apply/applycont/$', views.choices, name='applycont'),
               	url(r'^login/$', views.login, name='login'),
               	url(r'^login/courses2/$', views.courses2, name='course2'),]
