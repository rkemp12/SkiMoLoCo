from django.views.generic import TemplateView
from scraping.models import MountainDates
from django.shortcuts import render
from scraping.tasks import mountain_rss

class HomePageView(TemplateView):
	template_name = 'home.html'

def mountain_details(request):
	mountain_rss()
	dates_list = MountainDates.objects.all()
	return render(request, 'resorts_view.html',
	{'dates_list': dates_list})
	 

class LocationPageView(TemplateView):
	template_name = 'location_directions.html'

class LocationPageView2(TemplateView):
	template_name = 'location_directions_2.html'

class LocationPageView3(TemplateView):
	template_name = 'location_directions_3.html'

class LocationPageView4(TemplateView):
	template_name = 'location_directions_4.html'