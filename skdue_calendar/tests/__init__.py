import unittest

def suite():   
    return unittest.TestLoader().discover("skdue_calendars.tests", pattern="*.py")