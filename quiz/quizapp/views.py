from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Myusers, Movies
from django.contrib.auth.models import User

from django.http import HttpResponse


def login(request):
    if request.user.is_authenticated:
        pk=1
        return render(request, 'choose.html', {'pk':pk})
    else:
        return render(request, 'index.html')

@login_required
#This function is messed up. Needs to be fixed asap.//kkc
def choose(request):
    
    player = request.user
    name = player.username
    case = 0
    prk = 1
    try:
        
        crap = Myusers.objects.get(email=player.email)
        if crap.choice is None:
    #       case = 0
    #    else:
            case = 1
        else:
            name = crap.name  

    except Myusers.DoesNotExist:
        user = Myusers()
        user.name = player.username
        user.email = player.email
        user.save()
        
        case = 0
        


    
    if case is 0:
        firsttime = 1
        return render(request, 'choose.html', {'name':name, 'firsttime':firsttime, 'pk':prk})

    firsttime = 0

 #   name = crap.choice
    

    return render(request, 'choose.html', {'name':name, 'firsttime':firsttime, 'pk':prk})


@login_required
def questionmovies(request, pk):

    
    user = request.user
    player = Myusers.objects.get(email=user.email)

    qno = player.pointsfactor
    qno = qno+1
    qno = str(qno)

    question = get_object_or_404( Movies, pk = qno)



    if request.method == 'POST':
        
        
        answer = request.POST.get('Answer')
        decision = question.check_ans(answer, question)
        if (decision == 1):
            
            player.pointsfactor= player.pointsfactor+1
            player.save()
            qno = player.pointsfactor
            qno = qno+1
            qno = str(qno)
            
        #    pk = int(pk)
        #    pk = pk+1
        #    pk = str(pk)
            questionnext = get_object_or_404( Movies, pk = qno)
       #     return HttpResponse("correct ans!")
            return render(request,'questions.html',{'question':questionnext, 'pk':qno})

        else :              
            return render(request, 'questions.html',{'question':question, 'pk':qno})
    
    else:
        return render(request, 'questions.html',{'question':question, 'pk':qno})
     
    



    
    return render(request, 'questions.html',{'question':question, 'pk':pk})


