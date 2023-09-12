from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import MINUTES, PeriodicTask, CrontabSchedule, PeriodicTasks
import json
from dashboard.models import Request
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class BroadcastNotification(models.Model):
    message = models.TextField()
    broadcast_on = models.DateTimeField()
    sent = models.BooleanField(default=False)
    request_for=models.ForeignKey(Request,on_delete=models.CASCADE)
    # reciver=models.ForeignKey(User,on_delete=models.CASCADE)
    # reciver_id=models.ForeignKey(User,on_delete=models.CASCADE)
    # reciver_id_id=models.ForeignKey(User,on_delete=models.CASCADE , default=None) 
    class Meta:
        ordering = ['-broadcast_on']
    
    def __str__(self):
        return self.message[:40] + " ..."

@receiver(post_save, sender=BroadcastNotification)
def notification_handler(sender, instance, created, **kwargs):
    # call group_send function directly to send notificatoions or you can create a dynamic task in celery beat
    if created:
        schedule, created = CrontabSchedule.objects.get_or_create(hour = instance.broadcast_on.hour, minute = instance.broadcast_on.minute,
                                                                day_of_month = instance.broadcast_on.day, month_of_year = instance.broadcast_on.month)
        task = PeriodicTask.objects.create(crontab=schedule, name="broadcast-notification-"+str(instance.id), task="notification.tasks.broadcast_notification",
                                            args=json.dumps((instance.id,)))

    # if not created:   # if updated