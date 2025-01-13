from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def room(request):
    return render(request, "room.html")

def rooms(request, r_id):
    return render(request, "rooms.html", {
        "r_id": r_id
    })

