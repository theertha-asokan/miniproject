from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def loginn(request):
    return render(request, 'login.html')