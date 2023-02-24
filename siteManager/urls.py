from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views
app_name = 'siteManager'

urlpatterns = [
    path('/add_event', PostEventView),
    path('/view_event', GetEventsView),
    # path('/add_new', PostNewsView),
    # path('/view_new', GetNewsView),
    path('/contact_us', ContactUs),
    path('/single_event/<int:id>', SingleEventView),
    path('/delete_event/<int:id>', DeleteEvent),
]
