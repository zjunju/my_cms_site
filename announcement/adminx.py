import xadmin
from .models import Announcement, Plan

class AnnouncementAdmin(object):
    list_display = ['sender', 'receiver', 'text']
    model_icon = 'fa fa-bell'

xadmin.site.register(Announcement, AnnouncementAdmin)


class PlanAdmin(object):
    list_display = ['title', 'sender', 'start_time', 'stop_time']
    list_filter = ['title', 'sender', 'start_time', 'stop_time']
    search_fileds = ['title', 'sender']
    model_icon = 'fa fa-calendar-o'
xadmin.site.register(Plan,PlanAdmin)
