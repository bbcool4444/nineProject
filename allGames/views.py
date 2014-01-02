from django.shortcuts import render_to_response
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template import RequestContext
from allGames.models import Game, Sponsor, Recommend, Comment

def index(request):
    recommends = Recommend.objects.order_by('pub_date')[:3]
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

def comments(request):
    games = Game.objects.all()

    return render_to_response('allGames/comment_detail.html', locals())

def post(request):
    user = request.POST['name']
    game = Game.objects.get(name=request.POST['game_name'])
    context = request.POST['comment']
    comment = Comment(user=user, game=game, context=context)

    return render_to_response('comments/posted.html', locals())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/allGames/")
    else:
        form = UserCreationForm()
    return render_to_response('registration/register.html', {'form': form})

def profile(request):
    return render_to_response('accounts/profile.html', locals(), context_instance=RequestContext(request))
