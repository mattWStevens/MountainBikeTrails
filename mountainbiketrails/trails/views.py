from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Trail

TrailForm = modelform_factory(Trail, exclude=[])

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
    return render(request, "trails/detail.html", {"trail": trail})