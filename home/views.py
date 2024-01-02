from django.shortcuts import render

# Create your views here.

def index(request):
    """" Renders home page """
    return render(request, 'home/index.html')