from django import forms
from .models import Player, Match

from django.forms import formset_factory

POSITION_CHOICES = [
    ('Forward', 'Forward'),
    ('Centre', 'Centre'),
    ('Defence', 'Defence'),
    ('Goalie', 'Goalie'),
]

class PlayerForm(forms.Form):
    name = forms.CharField(max_length=100)
    position = forms.ChoiceField(choices=POSITION_CHOICES)

PlayerFormSet = formset_factory(PlayerForm, min_num=5, max_num=12)


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['date', 'half_length', 'substitution_interval', 'field_players_count']


class SubstitutionForm(forms.Form):
    player_out = forms.ModelChoiceField(queryset=Player.objects.all())
    player_in = forms.ModelChoiceField(queryset=Player.objects.all())
    time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': 'HH:MM'}))
    period = forms.ChoiceField(choices=[('first', 'First Half'), ('second', 'Second Half')])
