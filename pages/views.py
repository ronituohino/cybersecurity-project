from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Message

@login_required
def addMessage(request):
    if request.user.username == "alice":
        target = User.objects.get(username=request.POST.get('to'))
    else:
        target = User.objects.get(username="alice")
    Message.objects.create(source=request.user, target=target, content=request.POST.get('content'))
    return redirect('/')

@login_required
def index(request):
    messages = Message.objects.filter(Q(source=request.user) | Q(target=request.user))

    is_alice = request.user.username == "alice"
    users = users = User.objects.exclude(pk=request.user.id)
    
    return render(request, "pages/index.html", { "messages": messages, "is_alice": is_alice, "users": users})
