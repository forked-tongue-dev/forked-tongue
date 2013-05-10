from tastypie import fields
from tastypie.resources import ModelResource
from torrents.models import Torrent, Category


def download_torrent(request):
    pass

def upload_torrent(request):
    """
    Handles file upload from a user and waits for torrent to be added to the processing queue.
    if the job can't be added return a status code to try again later.
    If the job was added, return status 202 for "Accepted".
    """

    def _pass_torrent_to_queue(torrent_file, torrent_data_dict):
        """
        sends torrent to be processed by a backend and avoid heavy lifting in views.
        returns success if added to queue correctly, else return fail and output warning to user.

        """
        pass

    pass

def search_torrents(request):
    pass


class CategoryResource(ModelResource):

    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'

class TorrentResource(ModelResource):
    torrent = fields.FileField('torrent')
    group = fields.ManyToManyField(CategoryResource, 'groups')

    def dehydrate_torrent(self, bundle):
        return bundle.obj.torrent.url

    class Meta:
        queryset = Torrent.objects.all()
        resource_name = 'torrent'