from django.shortcuts import render

# Create your views here.

from .models import User


def index(request):
    users = User.objects.all()
    beginnum = 10001
    usernamelist = []
    for user in users:
        usernamelist.append(user.username)
    for n in range(beginnum, 10200):
        if str(n) not in usernamelist:
            now_username = n
            break
    return render(request, 'index.html', {'users': users, 'now_username': now_username})
