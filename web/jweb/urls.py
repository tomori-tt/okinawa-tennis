from django.urls import path
from .views import IndexView, SukejuruView, TournamentView, ContactView

urlpatterns = [
    path('',IndexView.as_view()),
    path('sukeju-ru/',SukejuruView.as_view()),
    path('tournament/',TournamentView.as_view()),
    path('Contact/',ContactView.as_view()),
]

