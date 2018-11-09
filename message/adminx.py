import xadmin
from .models import Message

class MessageAdmin(object):
    list_display = ['sender', 'receiver', 'content', 'send_time']
    list_filter = ['sender__username','receiver__username', 'is_read', 'send_time', 'content']
    search_fields = ['sender__username','receiver__username', 'content']
    list_per_page = 10
    model_icon = "fa fa-comments"
    ordering = ['-send_time']

xadmin.site.register(Message, MessageAdmin)
