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

    def post(self, request):
        """Create new calendar
        
        Args:
            calendar_data: a dict consist of,
                - name: calendar name
                - optional:
                    - is_test: True for testing, False otherwise

        Returns:
            dict: response data
        """
        calendar_data = request.data
        if Calendar.is_valid(calendar_data):
            slug = Calendar.generate_slug(calendar_data["name"])
            new_calendar = Calendar(
                name = calendar_data["name"],
                slug = slug
            )
            if  "is_test" not in calendar_data.keys() or calendar_data["is_test"].lower() != "true":
                new_calendar.save()
            serializers = CalendarSerializer(new_calendar)
            data = serializers.data
            data["status"] = "success" # add created status
            data["msg"] = "calendar created"
            return Response(data)
        return Response({"status": "failed", "msg": "invalid calendar"})


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
        """Create new calendar
        
        Args:
            event_data: a dict consist of,
                - name: calendar event name
                - description: description of event
                - start_date: format (YYYY-MM-DD hh:mm:ss)
                - end_date: same format as start_date
                - optional:
                    - is_test: True for testing, False otherwise

        Returns:
            dict: response data
        """
        event_data = request.data
        if CalendarEvent.is_valid(event_data, calendar_slug):
            calendar = Calendar.objects.get(slug=calendar_slug)
            slug = CalendarEvent.generate_slug(event_data["name"]) 
            new_event = CalendarEvent(
                calendar=calendar,
                name = event_data["name"],
                slug = slug,
                description = event_data["description"],
                start_date = event_data["start_date"],
                end_date = event_data["end_date"]
            )
            # When testing, this event will not included in database
            if "is_test" not in event_data.keys() or event_data["is_test"].lower() != "true":
                new_event.save()
            new_event = CalendarEvent.objects.get(calendar__slug=calendar_slug, slug=slug)
            serializers = CalendarEventSerializer(new_event)
            data = serializers.data
            data["status"] = "success"
            data["msg"] = "calendar event created"
            # id of event will be null when `is_test` == true
            return Response(data)
        return Response({"status": "failed", "msg": "invalid calendar event"})


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
