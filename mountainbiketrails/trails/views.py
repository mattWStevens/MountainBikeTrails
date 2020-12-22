from django.shortcuts import render, get_object_or_404, redirect
from .models import Trail
from .forms import TrailForm

def add(request):
    if request.method == "POST":
        form = TrailForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = TrailForm()

    return render(request, "trails/add.html", {"form": form})

def detail(request, id):
    trail = get_object_or_404(Trail, pk=id)

    length_string = str(trail.length) if str(round(trail.length % 1, 1)) != "0.0" else str(int(trail.length))

    length_string = length_string + " mile" if length_string == "1" else length_string + " miles"

    return render(request, "trails/detail.html", {"trail": trail, "length_string": length_string})