from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name="add"),
    path('detail/<int:id>', views.detail, name="detail")
]
