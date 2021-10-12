from calendar import calendar
from datetime import datetime
from django.db import models


class Calendar(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'

    @classmethod
    def is_valid(self, calendar_data: dict) -> bool:
        """Validate calendar data for create new calendar.
        
        Args:
            calendar_data: dict for calendar creation

        Returns:
            bool: True, if calendar name does not exist, False otherwise.
        """
        slug = Calendar.generate_slug(calendar_data["name"])
        try:
            _ = Calendar.objects.get(slug=slug)
        except:
            return True
        return False

    @classmethod
    def generate_slug(self, name: str) -> str:
        """Generate slug for calendar from name of the calendar"""
        return '-'.join(name.lower().split())


class CalendarEvent(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        ordering = ('-start_date',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.calendar.slug}/{self.slug}'

    @classmethod
    def is_valid(self, event_data: str, calendar_slug) -> bool:
        """Validate calendar event from calendar event data
        
        Args:
            event_data: dict for calendar event data
            calendar_slug: slug of calendar

        Returns:
            bool: False, if calendar_slug does not exist or start_date < end_date, True otherwise.
        """
        slug = CalendarEvent.generate_slug(event_data["name"])
        is_same = False
        try:
            calendar = Calendar.objects.get(slug=calendar_slug)
            for event in calendar.calendarevent_set.all():
                print(event.slug, slug)
                if event.slug == slug:
                    is_same = True
                    break
            print("is same", is_same)
        except:
            return False # calendar not found

        start_date = datetime.strptime(event_data["start_date"], "%Y-%m-%d %H:%M:%S")
        end_date = datetime.strptime(event_data["end_date"], "%Y-%m-%d %H:%M:%S")
        return start_date < end_date and not is_same
        

    @classmethod
    def generate_slug(self, name: str):
        return '-'.join(name.lower().split())