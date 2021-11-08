from django.views.generic import TemplateView


class HomePageView(TemplateView):
	template_name = 'home.html'

class ResortsPageView(TemplateView):
	template_name = 'resorts_view.html'

class LocationPageView(TemplateView):
	template_name = 'location_directions.html'