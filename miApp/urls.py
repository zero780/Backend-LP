from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^participants/$', Participant_list.as_view(), name ='participants'),
    url(r'^participants/(?P<pk>[0-9]+)/$', Participant_detail.as_view()),

    url(r'^groups/$', Group_list.as_view(), name='groups'),
    url(r'^groups/(?P<pk>[0-9]+)/$', Group_detail.as_view()),
]