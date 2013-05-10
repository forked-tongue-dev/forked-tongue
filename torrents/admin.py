from django.contrib import admin
from torrents.models import Torrent, Category, Files

admin.site.register(Torrent)
admin.site.register(Category)
admin.site.register(Files)