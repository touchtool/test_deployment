from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.CalendarList.as_view()),
    path('<slug:calendar_slug>/', views.CalendarEventList.as_view()),
    path('<slug:calendar_slug>/<slug:event_slug>/', views.CalendarEventDetail.as_view()),
]
