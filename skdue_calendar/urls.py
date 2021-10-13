from django.urls import path, include

from skdue_calendar.models import CalendarEvent

from .views import CalendarList, CalendarEventList, CalendarEventDetail

app_name = "skdue_calendar"
urlpatterns = [
    path('', CalendarList.as_view(), name="list"),
    path('<slug:calendar_slug>/', CalendarEventList.as_view(), name="event_list"),
    path('<slug:calendar_slug>/<slug:event_slug>/', CalendarEventDetail.as_view(), name="event_detail"),
]
