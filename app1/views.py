from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def SignUp(request):
    print("Hello...")
    email = request.GET['email']
    psw = request.GET['pswname']
    return render(request, "index.html")


def abc(request):
    return HttpResponse("hello welcome to my python project session")