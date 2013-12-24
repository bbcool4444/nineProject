from django.shortcuts import render_to_response
from allGames.models import Game, Sponsor

def index(request):
    games = Game.objects.order_by('name')
    sponsoies = Sponsor.objects.all()

    return render_to_response('allGames/index.html', locals())
