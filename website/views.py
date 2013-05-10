from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from torrents.models import Torrent
from website.forms import LoginForm
from website.models import Mirrors


def index(request):
    recent_torrents = Torrent.objects.all()[:10]
    login_form = LoginForm()
    return render(request, 'index.html', {'torrents': recent_torrents, 'form':login_form})

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
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.isvalid():
            pass
    else:
        login_form = LoginForm()

def profile(request):
    pass