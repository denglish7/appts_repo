from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logoff/$', views.logoff, name='logoff'),
    url(r'^add_appt/$', views.add_appt, name='add_appt'),
    url(r'^appointments/(?P<id>\d+)$', views.show, name='my_show'),
    url(r'^update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name = 'my_destroy'),
]
