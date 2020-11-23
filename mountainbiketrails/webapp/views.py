from django.shortcuts import render
from trails.models import Trail

def home_page(request):
    return render(request, "webapp/index.html", {"trails": Trail.objects.all()})