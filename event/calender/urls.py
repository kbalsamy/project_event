from django.urls import path
from .views import EventList, EventDetail

urlpatterns = [

    path('eventslist', EventList.as_view(), name='events'),
    path('<int:pk>/', EventDetail.as_view(), name='event_detail')
]
