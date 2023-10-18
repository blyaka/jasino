from django.urls import path
from .views import GamesPageView, GamesDetailView, GamesSearchResultsListView, NvutiPageView, DoublePageView, CrashPageView, gamesDetail, gameStatus

urlpatterns = [
    path('', GamesPageView.as_view(), name='games_list'),
    path('<str:slug>', GamesDetailView.as_view(), name='gamesearch'),
    path('nvuti/', NvutiPageView.as_view(), name='game'),
    path('crash/', CrashPageView.as_view(), name='game'),
    path('double/', DoublePageView.as_view(), name='game'),
    path('search/', GamesSearchResultsListView.as_view(), name='games_search_results'),
    path('crash/game-status/', gameStatus, name='gameStatus'),
]