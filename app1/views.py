from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def SignUp(request):
    print("Signup method is working...")
    a=10
    b=20
    print(a+b)
    return render(request, "index.html")1


def abc(request):
    return HttpResponse("hello welcome to my python project session")