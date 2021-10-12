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
    calendar = models.ForeignKey(Calendar, related_name="calendars", on_delete=models.CASCADE)
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
    def generate_slug(self, name: str):
        return '-'.join(name.lower().split())