from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("dark/", views.home_dark, name="home_dark"),
    path("announcement/", views.announcement, name="announcement"),
    path("howto/", views.howto, name="howto"),
    path("creators/", views.creators, name="creators"),
    path("ranking/", views.ranking, name="ranking"),
]
