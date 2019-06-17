from django.db import models


class Event(models.Model):

    EVENT_STATUS = (('upcoming', 'Upcoming'), ('completed', 'Completed'), ('cancelled', 'Cancelled'),
                    ('postponed', 'Postponed'))

    name = models.CharField(max_length=50)
    eventOn = models.DateField()
    locationAt = models.CharField(max_length=50)
    description = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=EVENT_STATUS, default='upcoming')

    def __str__(self):

        return self.name
