from django.shortcuts import render, get_object_or_404
from .models import Trail

def add(request):
    return render(request, "trails/add.html")

def detail(request, id):
    trail = get_object_or_404(Trail, pk=id)
    return render(request, "trails/detail.html", {"trail": trail})