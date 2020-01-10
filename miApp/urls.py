from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^participants/$', Participant_list.as_view(), name ='participants'),
    url(r'^participants/(?P<pk>[0-9]+)/$', Participant_detail.as_view()),

    url(r'^groups/$', Group_list.as_view(), name='groups'),
    url(r'^groups/(?P<pk>[0-9]+)/$', Group_detail.as_view()),

    url(r'^organizers/$', Organizer_list.as_view(), name='organizers'),
    url(r'^organizers/(?P<pk>[0-9]+)/$', Organizer_detail.as_view()),

    url(r'^events/$', Event_list.as_view(), name='events'),
    url(r'^events/(?P<pk>[0-9]+)/$', Event_detail.as_view()),

    url(r'^memberships/$', Membership_list.as_view(), name='memberships'),
    url(r'^memberships/(?P<pk>[0-9]+)/$', Membership_detail.as_view()),

    url(r'^event_stages/$', Event_Stage_list.as_view(), name='event_stages'),
    url(r'^event_stages/(?P<pk>[0-9]+)/$', Event_Stage_detail.as_view()),

    url(r'^event_constraint/$', Event_constraint_list.as_view(), name='event_constraint'),
    url(r'^event_constraint/(?P<pk>[0-9]+)/$', Event_constraint_detail.as_view()),

    url(r'^notifications/$', Notification_list.as_view(), name='notifications'),
    url(r'^notifications/(?P<pk>[0-9]+)/$', Notification_detail.as_view()),
]