from django.shortcuts import render

# Create your views here.
def subway(request):
    return render(request, "configs/subway.html")

def logins(request):
    return render(request, "configs/logins.html")