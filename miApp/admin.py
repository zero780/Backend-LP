from django.contrib import admin
from .models import Participant,Group,Organizer,Event,Membership,Event_Stage,Event_constraint,Notification

# Register your models here.

admin.site.register(Participant)
admin.site.register(Group)
admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(Membership)
admin.site.register(Event_Stage)
admin.site.register(Event_constraint)
admin.site.register(Notification)
