# imports

from django.shortcuts import render

# views


def home(request):
    return render(request, 'home.html')
