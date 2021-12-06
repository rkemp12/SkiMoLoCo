from django.views.generic import TemplateView
from scraping.models import MountainDates

class HomePageView(TemplateView):
	template_name = 'home.html'

class ResortsPageView(TemplateView):
		
	def get_context_data(self, **kwargs):
		
		context = super().get_context_data(**kwargs)
		data = MountainDates.objects.filter(mountain='snowbowl')
		context['snowbowlDate'] = data

		
		if MountainDates.mountain == 'snowbowl':
			context['date'] = MountainDates.winter_season
		elif MountainDates.mountain == 'bigsky':
			context['date'] = MountainDates.winter_season
		
		return context	
	
	
	template_name = 'resorts_view.html'

class LocationPageView(TemplateView):
	template_name = 'location_directions.html'

class LocationPageView2(TemplateView):
	template_name = 'location_directions_2.html'

class LocationPageView3(TemplateView):
	template_name = 'location_directions_3.html'

class LocationPageView4(TemplateView):
	template_name = 'location_directions_4.html'