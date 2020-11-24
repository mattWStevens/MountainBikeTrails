from django.shortcuts import render

# Create your views here.
def add(request):
    return render(request, "trails/add.html")

def detail(request):
    return render(request, "trails/detail.html")