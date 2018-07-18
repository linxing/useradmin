from django.shortcuts import render

# Create your views here.

from .models import User


def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users':users})
