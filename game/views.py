from django.shortcuts import render_to_response
from game.models import Game

def index(response):
    games = Game.objects.order_by('title')

    return render_to_response('game/index.html', locals())

def show(response, game_name):
    game = Game.objects.get(title=game_name)

    return render_to_response('game/show.html', locals())
