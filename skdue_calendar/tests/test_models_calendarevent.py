from calendar import calendar
from datetime import datetime, timedelta

from django.test import TestCase
from skdue_calendar.models import Calendar, CalendarEvent


class CalendarEventModelTest(TestCase):
    def setUp(self):
        for i in range(3):
            name = f"calendar {i}"
            slug = Calendar.generate_slug(name)
            calendar = Calendar(name=name, slug=slug)
            calendar.save()

    def test_1(self):
        self.assertTrue(1)