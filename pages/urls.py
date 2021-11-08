from django.urls import path
from .views import (HomePageView, ResortsPageView, LocationPageView)


urlpatterns = [
path('location/', LocationPageView.as_view(), name='location_directions'),
path('resorts/', ResortsPageView.as_view(), name='resorts_view'),
path('', HomePageView.as_view(), name='home'),

]
