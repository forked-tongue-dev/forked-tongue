import os
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models import Sum
from django.forms import ChoiceField
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

    class Meta:
        abstract = True


class MusicTorrent(Torrent):

    FORMAT_TYPES = (
        ('mp3', 'MP3'),
        ('flac', 'FLAC'),
        ('aac', 'AAC'),
        ('ac3', 'AC3'),
        ('dts', 'DTS'),
    )

    BITRATE_TYPES = (
        ('192', '192'),
        ('apsvbr', 'APS (VBR)'),
        ('v2vbr', 'V2 (VBR)'),
        ('v1vbr', 'V1 (VBR)'),
        ('256', '256'),
        ('apxvbr', 'APX (VBR)'),
        ('v0vbr', 'V0 (VBR)'),
        ('320', '320'),
        ('lossless', ('Lossless')),
        ('24bitlossless', ('24Bit Lossless')),
        ('v8vbr', 'V8 (VBR)'),
        ('other', ('Other')),

    )

    MEDIA_TYPES = (
        ('cd', 'CD'),
        ('dvd', 'DVD'),
        ('vinyl', ('Vinyl')),
        ('soundboard', ('Soundboard')),
        ('sacd', 'SACD'),
        ('dat', 'DAT'),
        ('cassette', ('Cassette')),
        ('web', 'WEB'),
        ('bluray', 'Blu-Ray'),
    )

    RELEASE_TYPES = (
        ('album', ('Album')),
        ('soundtrack', ('Soundtrack')),
        ('ep', ('EP')),
        ('anthology', ('Anthology')),
        ('compilation', ('Compilation')),
        ('djmix', ('DJ Mix')),
        ('single', ('Single')),
        ('livealbum', ('Live Album')),
        ('remix', ('Remix')),
        ('bootleg', ('Bootleg')),
        ('interview', ('Interview')),
        ('mixtape', ('Mixtape')),
        ('unknown', ('Unknown'))
    )
    # uuid = UUIDField(primary_key=True)
    # name = models.CharField(max_length=100)
    # description = models.TextField()
    # torrent = models.FileField(upload_to=torrent_storage(), max_length=2048, storage=fs)
    # groups = models.ManyToManyField('Category')

    file_format = ChoiceField(choices=FORMAT_TYPES)
    bitrate = ChoiceField(choices=BITRATE_TYPES)
    media = ChoiceField(choices=MEDIA_TYPES)
    release = ChoiceField(choices=RELEASE_TYPES)

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