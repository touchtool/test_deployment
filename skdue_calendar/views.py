from django.http.response import Http404

# from rest_framework.parsers import MultiPartParser 
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

    def post(self, request, calendar_slug, format=None):
        event_data = request.data
        calendar = Calendar.objects.get(slug=calendar_slug)
        event_data["slug"] = CalendarEvent.generate_slug(event_data["name"]) 
        new_event = CalendarEvent(
            calendar=calendar,
            name = event_data["name"],
            slug = event_data["slug"],
            description = event_data["description"],
            start_date = event_data["start_date"],
            end_date = event_data["end_date"]
        )
        # When testing, this event will not included in database
        if event_data["is_test"].lower() != "true":
            new_event.save()
        serializers = CalendarEventSerializer(new_event)
        # id of event will be null when `is_test` == true
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