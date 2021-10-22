from django.test import TestCase
from skdue_calendar.utils import generate_slug


class UtilsTests(TestCase):
    def test_generate_slug(self):
        """Test that generate_slug returns correct slug"""
        names = ["event 1", "EvnTR 2", "evBMr 3 AND 5"]
        expects = ["event-1", "evntr-2", "evbmr-3-and-5"]
        for name, expect in zip(names, expects):
            with self.subTest():
                self.assertEqual(expect, generate_slug(name))
        names = ["caLendar 1", "CaleENDAR TWO", "calendar 3 and 4"]
        expects = ["calendar-1", "caleendar-two", "calendar-3-and-4"]
        for name, expect in zip(names, expects):
            with self.subTest():
                self.assertEqual(expect, generate_slug(name))