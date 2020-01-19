from django.db import models
from django import forms
from django.contrib import auth


class Organizer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=30)
    country = models.CharField(max_length=30, default="Ecuador")
    city = models.CharField(max_length=30)
    status = models.BooleanField(null=True, default=True)
    user = models.OneToOneField(auth.models.User, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (self.id, self.name)

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    modality_choices = [("Presencial", "Presencial"),
                        ("Semi-Presencial", "Semi-Presencial"),
                        ("Remota", "Remota")]
    modality = models.CharField(max_length=50, choices=modality_choices)
    image = models.ImageField(null=True, upload_to ='miApp/media')
    description = models.TextField(null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    availability = models.BooleanField(null=True, default=True)
    status = models.BooleanField(null=True, default=True)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s: %s' % (self.id, self.name)

class Event_Stage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (self.id, self.name)

class Participant(models.Model):
    id=models.AutoField(primary_key=True)
    names = models.CharField(max_length=50)
    last_names = models.CharField(max_length=50)
    email= models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    country = models.CharField(max_length=30, default='Ecuador')
    city = models.CharField(max_length=30)
    status = models.BooleanField(null=True, default=True)
    notification_subscriptions = models.ManyToManyField(Event_Stage, through='Notification')
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s %s' % (self.id, self.last_names, self.names)

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    join_code = models.CharField(max_length=50, null=True)
    status = models.BooleanField(null=True, default=True)
    participants = models.ManyToManyField(Participant, through='Membership')

    def __str__(self):
        return '%s: %s' % (self.id, self.name)

class Membership(models.Model):
    id = models.AutoField(primary_key=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: Participante: %s\nGrupo: %s\nEvento: %s' % (self.id, self.participant,self.group,self.event)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['participant', 'group', 'event'], name='unique_membership')
        ]

class Event_constraint(models.Model):
    id = models.AutoField(primary_key=True)
    min_group_size = models.IntegerField(null=True, default=None)
    max_group_size = models.IntegerField(null=True, default=None)
    min_participant_age = models.IntegerField(null=True, default=None)
    max_participant_age = models.IntegerField(null=True, default=None)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: Evento: %s' % (self.id, self.event)

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event_stage = models.ForeignKey(Event_Stage, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: Participante: %s\nEvento: %s' % (self.id, self.participant, self.event_stage)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['participant', 'event_stage'], name='unique_notification')
        ]
