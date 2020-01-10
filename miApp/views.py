from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import generics

# Create your views here.

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

