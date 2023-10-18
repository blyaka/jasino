from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import Game
from django.db.models import Q
from accounts.models import CustomUser
from django.http import HttpResponseRedirect
import json
class GamesPageView(ListView):
    model = Game
    context_object_name = 'games_list'
    template_name = 'games/games_list.html'

class GamesDetailView(DetailView):
    model = Game
    context_object_name = 'game'
    template_name = 'games/game_detail.html'


def gamesDetail(request):
    return HttpResponseRedirect(request.slug)

class NvutiPageView(TemplateView):
    model = Game
    template_name = 'games/nvuti.html'

class DoublePageView(TemplateView):
    model = Game
    template_name = 'games/double.html'

class CrashPageView(TemplateView):
    model = Game
    template_name = 'games/crash.html'


class GamesSearchResultsListView(ListView):
    model = Game
    context_object_name = 'games_list'
    template_name = 'games/games_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Game.objects.filter(Q(name__icontains=query))


def gameStatus(request):
    with open('templates/games/crash-ready-to-play.json') as f:
        response = json.load(f)

    return JsonResponse(response)

