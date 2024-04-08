from django.urls import path
from .views import HomeView, MatchCreateView, SubstitutionCreateView, enter_players

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('match/create/', MatchCreateView.as_view(), name='match_create'),
    path('substitution/create/', SubstitutionCreateView.as_view(), name='substitution_create'),
    path('enter-players/', enter_players, name='enter_players'),
]
