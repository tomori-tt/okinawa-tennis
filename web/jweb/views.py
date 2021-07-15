from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name="index.html"

class SukejuruView(TemplateView):
    template_name="sukeju-ru.html"

class TournamentView(TemplateView):
    template_name="tournament.html"

class ContactView(TemplateView):
    template_name="Contact Us.html"
# Create your views here.
