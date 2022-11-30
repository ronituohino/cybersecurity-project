from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Message


@login_required
@csrf_exempt
def addMessage(request):
    if request.user.username == "alice":
        target = User.objects.get(username=request.POST.get("to"))
    else:
        target = User.objects.get(username="alice")
    Message.objects.create(
        source=request.user, target=target, content=request.POST.get("content")
    )
    return redirect("/")


def get_messages(user, limitToThree: bool):
    messages = sorted(
        Message.objects.filter(Q(source=user) | Q(target=user)),
        key=lambda m: m.time,
        reverse=True,
    )

    if limitToThree:
        return messages[0:3]
    return messages


@login_required
def index(request):
    messages = get_messages(request.user, True)
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
    messages = get_messages(user, False)
    # Fix broken access control
    # messages = get_messages(request.user, False)

    return render(request, "pages/messages.html", {"messages": messages})
