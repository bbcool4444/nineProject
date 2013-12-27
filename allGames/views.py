from django.shortcuts import render_to_response
from allGames.models import Game, Sponsor
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage

def index(request):
    games = Game.objects.order_by('name')

    page = int(request.GET.get('page', 1))
    after_range_num = 5
    before_range_num = 4

    try:
        page = int(request.GET.get('page', 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1

    paginator = Paginator(games, 2)
    try:
        game_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        game_list = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+before_range_num]

    return render_to_response('allGames/index.html', locals())

def show(request, game_pk):
    game = Game.objects.get(pk=game_pk)

    return render_to_response('allGames/show.html', locals())
