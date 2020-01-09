from django.db import models

# Create your models here.

class Participant(models.Model):
    id=models.AutoField(primary_key=True)
    names = models.CharField(max_length=50)
    last_names = models.CharField(max_length=50)
    username= models.CharField(max_length=30)
    email= models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField(default=None)
    age = models.IntegerField(default=None)
    country = models.CharField(max_length=30, default="Ecuador")
    city = models.CharField(max_length=30)
    status = models.BooleanField(default=True)

    def __str__(self):
        return '%s: %s %s' % (self.id, self.last_names,self.names)

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    join_code = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return '%s: %s' % (self.id, self.name)

class Organizer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username= models.CharField(max_length=30)
    email= models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    country = models.CharField(max_length=30, default="Ecuador")
    city = models.CharField(max_length=30)
    status = models.BooleanField(default=True)

    def __str__(self):
        return '%s: %s' % (self.id, self.name)

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    modality_choices = [("Presencial","Presencial"),
                        ("Semi-Presencial","Semi-Presencial"),
                        ("Remota","Remota"),]
    modality = models.CharField(max_length=50,choices=modality_choices)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None)
    availability = models.BooleanField
    status = models.BooleanField(default=True)
    organizer = models.ForeignKey(Organizer,on_delete=models.CASCADE)


    def __str__(self):
        return '%s: %s' % (self.id, self.name)

class Membership(models.Model):
    id = models.AutoField(primary_key=True)
    leader = models.CharField(max_length=150)
    creator = models.CharField(max_length=150)
    participant = models.ForeignKey(Participant,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)

    def __str__(self):
        return '%s: Participante: %s\nGrupo: %s\nEvento: %s' % (self.id, self.participant,self.group,self.event)

class Event_Stage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (self.id, self.name)

class Event_constraint(models.Model):
    id = models.AutoField(primary_key=True)
    min_group_size = models.IntegerField
    max_group_size = models.IntegerField
    min_participant_age = models.IntegerField
    max_participant_age = models.IntegerField
    event = models.ForeignKey(Event,on_delete=models.CASCADE)

    def __str__(self):
        return '%s: Evento: %s' % (self.id, self.event)

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event_stage = models.ForeignKey(Event_Stage,on_delete=models.CASCADE)

    def __str__(self):
        return '%s: Participante: %s\nEvento: %s' % (self.id, self.participant, self.event_stage)









