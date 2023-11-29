from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Photo)
admin.site.register(Likes)
admin.site.register(Comment)
