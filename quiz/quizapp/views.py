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
    
    try:
        x=player.email
        case = Myusers.objects.get(email=x)

    except Myusers.DoesNotExist:
        user = Myusers(name=player.first_name, email= player.email)
        
        case = None
        user.save()


    name = player.name
    if case is None:
        firsttime = 1
        return render(request, 'choose.html', {'name':name, 'firsttime':firsttime})

    firsttime = 0
    

    return render(request, 'choose.html', {'name':name, 'firsttime':firsttime})


@login_required
def questions(request):
    return render(request, 'questions.html')


