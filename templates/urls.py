from django.urls import path, include
from . import views

app_name = 'app_name_placeholder'

urlpatterns = [
    path('', views.index, name="index"),
]