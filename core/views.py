from django.shortcuts import render

# Create your views here.
def home(request):
    return render(
        request,
        "tabs/home.html",
        context={"dark": False},
    )


def home_dark(request):
    return render(
        request,
        "tabs/home.html",
        context={"dark": True},
    )


def announcement(request):
    return render(request, "tabs/announcement.html")


def howto(request):
    return render(request, "tabs/howto.html")


def creators(request):
    return render(request, "tabs/creators.html")


def ranking(request):
    return render(request, "tabs/ranking.html")
