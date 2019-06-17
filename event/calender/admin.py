from django.contrib import admin
from .models import Event


class EventsAdmin(admin.ModelAdmin):

    ordering = ['eventOn', ]
    list_display = ['name', 'eventOn', 'status']


admin.site.register(Event, EventsAdmin)
