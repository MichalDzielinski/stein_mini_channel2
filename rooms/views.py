from django.shortcuts import render
from .models import Room
from django.contrib.auth.decorators import login_required

@login_required
def rooms(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'rooms/rooms.html', context)

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    context = {'room': room}
    return render(request, 'rooms/room.html', context)
