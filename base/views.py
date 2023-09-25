from django.shortcuts import render

# Create your views here.


rooms = [
    {'id':1, 'name': 'Lets learn python!'},
    {'id':2, 'name': 'Design with me'},
    {'id':3, 'name': 'Frontend developers'},
]


def home(request):
    context = {'rooms': rooms} # no idea what this is for
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
        context = {'room': room} # no idea what this is for
    return render(request, 'base/room.html', context)