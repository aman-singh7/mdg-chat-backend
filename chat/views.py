from django.shortcuts import render

unpaired = False
latest_channel_number = 0


def lobby(request):
    global unpaired, latest_channel_number
    if (not unpaired):
        latest_channel_number += 1
    unpaired = not unpaired
    return render(request, 'chat/lobby.html', {
        'room_name': str(latest_channel_number)
    })


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
