from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Lets learn js'},
    {'id': 3, 'name': 'Lets learn java'},
]


def home(request):
    return render(request, "base/home.html")

def room(request):
    return render(request, "base/room.html", {
        'rooms': rooms
    })





