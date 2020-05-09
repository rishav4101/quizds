from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Myusers
from django.contrib.auth.models import User

from django.http import HttpResponse


def login(request):
    if request.user.is_authenticated:
        return render(request, 'choose.html')
    else:
        return render(request, 'index.html')

@login_required
def choose(request):
    
    player = User.objects.first()
    name = player.email
    try:
        
        case = Myusers.objects.get(email=player.email)


    except Myusers.DoesNotExist:
        user = Myusers()
        user.name = player.username
        user.email = player.email
        user.save()
        
        case = None
        


    
    if case is None:
        firsttime = 1
        return render(request, 'choose.html', {'name':name, 'firsttime':firsttime})

    firsttime = 0
    

    return render(request, 'choose.html', {'name':name, 'firsttime':firsttime})


@login_required
def questions(request):
    player = User.objects.first()
    name = player.username
    return render(request, 'questions.html',{'name':name})


