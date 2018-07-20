from django.shortcuts import render

# Create your views here.

from .models import User
import datetime

def index(request):
    users = User.objects.all()
    beginnum = 10001
    usernamelist = []
    totalincome = 0
    averge_perday = 0
    for user in users:
        usernamelist.append(user.username)
        totalincome += int(user.price)
    for n in range(beginnum, 10200):
        if str(n) not in usernamelist:
            now_username = n
            break
    firstday = datetime.datetime(2017, 12, 1)
    now = datetime.datetime.now()
    days = (now - firstday).days
    averge_perday = totalincome // days
    return render(request, 'index.html', {'users': users, 'now_username': now_username, 'totalincome': totalincome, 'averge_perday':averge_perday})
