from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from accounts.models import CustomUser
from django.shortcuts import render
from django.db.models import F
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from games.models import Game



class HomePageView(TemplateView):
    template_name = 'home.html'
    def all_users(self):
        return CustomUser.objects.order_by('-balance')[:5]
    def all_games(self):
        return Game.objects.all()
class AboutPageView(TemplateView):
    template_name = 'about.html'

class ProfilePageView(DetailView):
    model = CustomUser
    context_object_name = 'profile'
    template_name = 'profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.username}\'s profile'
        return context

class BalancePageView(TemplateView):
    model = CustomUser
    template_name = 'balance.html'

def deposit(request):
    if request.method == 'POST':
        user = request.user
        CustomUser.deposit(user, request.POST.get('deposit', 0))
    return HttpResponseRedirect('/balance')




class UserListPageView(ListView):
    model = CustomUser
    context_object_name = 'user_list'
    template_name = 'home.html'






