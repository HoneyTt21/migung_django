from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("login/", views.home, name="login"),
    path("logout/", views.home, name="logout"),
    path("history/", views.home, name="history"),
]
