from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^process/$', views.process),     # This line has changed!
    url(r'^checkout/$', views.checkout)     # This line has changed!
]