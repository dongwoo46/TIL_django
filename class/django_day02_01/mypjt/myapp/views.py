from django.shortcuts import render

# Create your views here.
def index(request):
    name = "dw"
    info = {
        "name": "dongwoo",
        "age" : 27
    }
    return render(request, "myapp/index.html", {'info': info})