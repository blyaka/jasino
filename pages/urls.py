from django.urls import path
from .views import HomePageView, AboutPageView, ProfilePageView, BalancePageView, deposit, UserListPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('profile/<uuid:pk>/', ProfilePageView.as_view(), name='profile'),
    path('balance/', BalancePageView.as_view(), name='balance'),
    path('deposit/', deposit, name='deposit'),
]

