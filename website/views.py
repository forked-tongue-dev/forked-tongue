from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from ForkedTongue.settings import PRIVATE_TRACKER, SITE_LOGO, SITE_NAME
from torrents.models import Torrent
from website.forms import LoginForm, SearchForm
from website.models import Mirrors
from django.contrib import auth


def index(request):
    if PRIVATE_TRACKER and not request.user.is_authenticated():
        login_form = LoginForm()
        return render(request, 'login.html', {'form':login_form, 'site_name': SITE_NAME, 'logo': SITE_LOGO})
    else:
        recent_torrents = Torrent.objects.all()[:10]
        search_form = SearchForm()
        return render(request, 'index.html', {'torrents':recent_torrents, 'site_name': SITE_NAME, 'logo': SITE_LOGO, 'search_form':search_form})

def select_mirror(request):
    if Mirrors.objects.filter(active=True).exists():
        mirror = Mirrors.objects.filter(active=True).order_by('?')[:1][0]
        return HttpResponseRedirect(mirror.url)
    else:
        messages.warning(request, "No Active Mirrors Found")
        return HttpResponseRedirect(reverse('index'))

def register(request):
    pass

def login(request):
    login_form = None
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=login_form.cleaned_data['login'], password=login_form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('index'))
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'form': login_form, 'site_name': SITE_NAME, 'logo': SITE_LOGO})

def profile(request):
    pass


def search(request):
    return render_to_response('search.html')