from django.shortcuts import render

# Create your views here.
def prologue(request):
    return render(
        request,
        "tabs/home.html",
        context={"dark": False},
    )