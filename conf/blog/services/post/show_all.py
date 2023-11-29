
from service_objects.services import Service
from blog.models import Photo


class BlogViewService(Service):

    def process(self):
        posts = Photo.objects.all()
        return posts
