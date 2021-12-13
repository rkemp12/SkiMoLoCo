from django.urls import path
from .views import HomePageView, LocationPageView, LocationPageView2, LocationPageView3, LocationPageView4, MapPageView
from . import views

urlpatterns = [
path('google_map/',MapPageView.as_view(), name='google_maps'),
path('location4/', LocationPageView4.as_view(), name='location_directions_4'),
path('location3/', LocationPageView3.as_view(), name='location_directions_3'),
path('location2/', LocationPageView2.as_view(), name='location_directions_2'),
path('location/', LocationPageView.as_view(), name='location_directions'),
#path('resorts/', ResortsPageView.as_view(), name='resorts_view'),
path('', HomePageView.as_view(), name='home'),
path('resorts/', views.mountain_details, name="resorts_view"),
]
