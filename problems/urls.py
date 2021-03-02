from django.urls import path
from . import views

app_name = "problems"
urlpatterns = [
    path("prologue/", views.prologue, name="prologue"),
]
