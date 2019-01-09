import uuid
from django.shortcuts import render
from .models import Message
from django.utils.safestring import mark_safe
import json


# Create your views here.

def index(request):
    uid4 = str(uuid.uuid4())
    return render(request, 'chat/index.html', {'uid4': uid4})
    # return render(request, 'chat/index.html', {})


def room(request, room_name):
    chat_messages = Message.objects.filter(group_name=room_name).order_by("created")[:100]
    return render(request, 'chat/room.html', {
        'chat_messages': chat_messages,
        'room_name': room_name
    # return render(request, 'chat/room.html', {
    #     'room_name': mark_safe(json.dumps(room_name))
    # 
    })

def dashboard(request):
    return render(request, 'chat/dashboard.html', {})