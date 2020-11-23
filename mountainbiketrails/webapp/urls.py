from django.urls import path, include
from .views import home_page

urlpatterns = [
    path('', home_page, name="home"),
    path('add', include('trails.urls'))
]
