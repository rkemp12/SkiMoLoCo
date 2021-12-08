from django.views.generic import TemplateView


class HomePageView(TemplateView):
	template_name = 'home.html'

class ResortsPageView(TemplateView):
	template_name = 'resorts_view.html'

class LocationPageView(TemplateView):
	template_name = 'location_directions.html'

class LocationPageView2(TemplateView):
	template_name = 'location_directions_2.html'

class LocationPageView3(TemplateView):
	template_name = 'location_directions_3.html'

class LocationPageView4(TemplateView):
	template_name = 'location_directions_4.html'

class MapPageView(TemplateView):
	template_name = 'google_maps.html'