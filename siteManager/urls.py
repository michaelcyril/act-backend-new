from django.urls import path
from .views import *

app_name = 'siteManager'

urlpatterns = [
    path('contact', ContactView.as_view()),
    path('application', ApplicationView.as_view()),
    path('event', EventView.as_view()),
]
