from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Participant)
admin.site.register(Group)
admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(Membership)
admin.site.register(Event_Stage)
admin.site.register(Event_constraint)
admin.site.register(Notification)
