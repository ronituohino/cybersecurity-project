from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Message


@login_required
def addMessage(request):
    if request.user.username == "alice":
        target = User.objects.get(username=request.POST.get("to"))
    else:
        target = User.objects.get(username="alice")
    Message.objects.create(
        source=request.user, target=target, content=request.POST.get("content")
    )
    return redirect("/")


def get_messages(user):
    messages = sorted(
        Message.objects.filter(Q(source=user) | Q(target=user)),
        key=lambda m: m.time,
        reverse=True,
    )
    return messages


@login_required
def index(request):
    messages = get_messages(request.user)
    is_alice = request.user.username == "alice"
    users = User.objects.exclude(pk=request.user.id)

    return render(
        request,
        "pages/index.html",
        {"messages": messages, "is_alice": is_alice, "users": users},
    )


@login_required
def messages(request, userid):
    user = User.objects.get(pk=userid)
    messages = get_messages(user)

    return render(request, "pages/messages.html", {"messages": messages})
