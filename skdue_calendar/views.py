from django.http.response import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Calendar, CalendarEvent
from .serializers import CalendarSerializer, CalendarEventSerializer


class CalendarList(APIView):
    def get(self, request, format=None):
        calendars = Calendar.objects.all()
        serializers = CalendarSerializer(calendars, many=True)
        return Response(serializers.data)


class CalendarEventList(APIView):
    def get_object(self, calendar_slug):
        try:
            return CalendarEvent.objects.filter(calendar__slug=calendar_slug)
        except CalendarEvent.DoesNotExist:
            raise Http404

    def get(self, request, calendar_slug, format=None):
        events = self.get_object(calendar_slug)
        serializers = CalendarEventSerializer(events, many=True)
        return Response(serializers.data)


class CalendarEventDetail(APIView):
    def get_object(self, calendar_slug, event_slug=None):
        try:
            if(event_slug):
                return CalendarEvent.objects.filter(calendar__slug=calendar_slug).get(slug=event_slug)
        except CalendarEvent.DoesNotExist:
            raise Http404

    def get(self, request, calendar_slug, event_slug, format=None):
        events = self.get_object(calendar_slug, event_slug)
        serializers = CalendarEventSerializer(events)
        return Response(serializers.data)        