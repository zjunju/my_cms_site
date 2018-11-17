import xadmin
from .models import Announcement

class AnnouncementAdmin(object):
    list_display = ['sender', 'receiver', 'text']
    model_icon = 'fa fa-bell'

xadmin.site.register(Announcement, AnnouncementAdmin)
