from StringIO import StringIO
import bencode
from celery import Celery

celery = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

@celery.task
def process_torrent(torrent_file, torrent_uuid):
    """
    Receives a torrent file from the job queue and decodes it into a python object.
    Once it is a python object it proceeds to add the database records that make up a Forked Tongue torrent.
    after all the data has been checked and added to the database, the torrent uuid is pushed for announce to connected
    clients.
    """
    from torrents.models import Files, Torrent

    torrent_data = bencode.bdecode(torrent_file)
    torrent_record = Torrent.objects.get(pk=torrent_uuid)
    if Files.objects.filter(torrent=torrent_record).exists():
        Files.objects.filter(torrent=torrent_record).delete()
    if 'files' in torrent_data['info']:
        for single_file in torrent_data['info']['files']:
            file_record = Files(torrent=torrent_record, filename=single_file['path'][0], filesize=single_file['length'])
            file_record.save()
    else:
        file_record = Files(torrent=torrent_record, filename=torrent_data['info']['name'], filesize=torrent_data['info']['length'])
        file_record.save()


@celery.task
def announce_torrent_to_clients(torrent_uuid):
    """
    Takes a torrent uuid and uses websocket? technology to relay that a new torrent is available for display.
    This allows a disconnected client to have a streaming torrent wall if they have registered for it.
    """
    pass

@celery.task
def announce_torrents_to_irc(torrent_uuid):
    """
    Takes a torrent UUID and makes an announcement on the site IRC channel so that automated bots can grab torrents.
    """
    pass