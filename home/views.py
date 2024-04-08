
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import MatchForm, SubstitutionForm
from .models import Match, Player
from django.urls import reverse_lazy
from .forms import PlayerFormSet

def enter_players(request):
    if request.method == 'POST':
        formset = PlayerFormSet(request.POST)
        if formset.is_valid():
            # Process form data
            for form in formset:
                if form.cleaned_data:
                    # Handle each player's data
                    pass
            # Redirect or render success message
    else:
        # Display form
        formset = PlayerFormSet()

    return render(request, 'enter_players.html', {'formset': formset})



def home(request):

    content = "Interchange App Test again"
    return HttpResponse(content, content_type="text/plain")


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['match_create_url'] = reverse_lazy('match_create')
        context['substitution_create_url'] = reverse_lazy('substitution_create')
        return context

class MatchCreateView(TemplateView):
    template_name = 'match_create.html'

    def get(self, request, *args, **kwargs):
        match_form = MatchForm()
        return render(request, self.template_name, {'match_form': match_form})

    def post(self, request, *args, **kwargs):
        match_form = MatchForm(request.POST)
        if match_form.is_valid():
            match = match_form.save()
            request.session['match_id'] = match.id  # Store match ID in session
            print(f"stored {match}")
            return redirect('substitution_create')
        return render(request, self.template_name, {'match_form': match_form})


class SubstitutionCreateView(TemplateView):
    template_name = 'substitution_create.html'

    def get(self, request, *args, **kwargs):
        substitution_form = SubstitutionForm()
        return render(request, self.template_name, {'substitution_form': substitution_form})

    def post(self, request, *args, **kwargs):
        substitution_form = SubstitutionForm(request.POST)
        if substitution_form.is_valid():
            match_id = request.session.get('match_id')
            if match_id:
                substitution = substitution_form.save(commit=False)
                substitution.match_id = match_id
                substitution.save()
                return redirect('substitution_create')
        return render(request, self.template_name, {'substitution_form': substitution_form})
