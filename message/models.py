from django.db import models
from users.models import User


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete = models.CASCADE,\
                                verbose_name='发送者', related_name='sender')
    receiver = models.ForeignKey(User, on_delete = models.CASCADE,\
                                verbose_name='接收者', related_name='receiver')
    send_time = models.DateTimeField(auto_now_add = True)
    is_read = models.BooleanField(default = False)

    class Meta:
        ordering = ['-send_time']
        verbose_name_plural = '消息'

    def __str__(self):
        return self.content