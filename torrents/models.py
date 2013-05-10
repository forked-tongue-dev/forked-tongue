import os
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models import Sum
from django_extensions.db.fields import UUIDField
from ForkedTongue import settings
from common.common import convert_bytes
from torrents.tasks import process_torrent


def torrent_storage():
    return "torrents/"

fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT))

class Torrent(models.Model):
    uuid = UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    torrent = models.FileField(upload_to=torrent_storage(), max_length=2048, storage=fs)
    groups = models.ManyToManyField('Category')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def total_filesize(self):
        total_bytes = Files.objects.filter(torrent=self.pk).aggregate(Sum('filesize'))
        return convert_bytes(total_bytes['filesize__sum'])

    def save(self, *args, **kwargs):
        super(Torrent, self).save(*args, **kwargs)
        process_torrent.delay(self.torrent.read(), self.uuid)

class Files(models.Model):
    uuid = UUIDField(primary_key=True)
    torrent = models.ForeignKey(Torrent)
    filename = models.TextField()
    filesize = models.PositiveIntegerField() #  In Bytes

    def __unicode__(self):
        return self.filename

    def __str__(self):
        return self.filename

class Category(models.Model):

    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name