# polling/urls.py

from django.urls import path
from mailroomapp.views import donations_view, donate_view

urlpatterns = [
    path('', donations_view, name="donations_index"),
    path('donate/<name>/', donate_view, name="donations_view"),
]
