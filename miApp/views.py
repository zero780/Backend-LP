from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

import hashlib


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

#API REST
#get, post
class Participant_list(generics.ListCreateAPIView):
    """
    List all participants, or create a new one.
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class Participant_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a participant.
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


#get, post
class Group_list(generics.ListCreateAPIView):
    """
    List all groups, or create a new one.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def perform_create(self, serializer):
        group = serializer.save()
        join_code = hashlib.md5(str(group.id).encode())
        group.join_code = join_code.hexdigest()[:6]
        group.save()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class Group_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a group.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#get, post
class Organizer_list(generics.ListCreateAPIView):
    """
    List all Organizers, or create a new one.
    """
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class Organizer_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an Organizer.
    """
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer


#get, post
class Event_list(generics.ListCreateAPIView):
    """
    List all Events, or create a new one.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'name',
        'location',
        'modality',
        'start_date',
        'end_date',
        'availability',
        'status',
        'organizer'
    ]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class Event_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an Event.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


#get, post
class Membership_list(generics.ListCreateAPIView):
    """
    List all Memberships, or create a new one.
    """
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class Membership_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Membership.
    """
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


#get, post
class Event_Stage_list(generics.ListCreateAPIView):
    """
    List all Event Stages, or create a new one.
    """
    queryset = Event_Stage.objects.all()
    serializer_class = Event_StageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class Event_Stage_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an Event Stage.
    """
    queryset = Event_Stage.objects.all()
    serializer_class = Event_StageSerializer


#get, post
class Event_constraint_list(generics.ListCreateAPIView):
    """
    List all Event constrainta, or create a new one.
    """
    queryset = Event_constraint.objects.all()
    serializer_class = Event_constraintSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class Event_constraint_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an Event constraint.
    """
    queryset = Event_constraint.objects.all()
    serializer_class = Event_constraintSerializer


#get, post
class Notification_list(generics.ListCreateAPIView):
    """
    List all Notifications, or create a new one.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class Notification_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Notification.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


