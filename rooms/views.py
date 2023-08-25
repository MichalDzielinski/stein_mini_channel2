from django.shortcuts import render
from .models import Room

def rooms(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'rooms/rooms.html', context)
