from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync,sync_to_async
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.



def index(request):
    return render(request , 'base.html' , {"room_name":"sultan"})

def test(request):
    channel_layer=get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_customer",{
            'type':'send_notification',
            'message':"Notification"
        }
    )
    return HttpResponse("Done customer")
