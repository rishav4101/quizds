from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Myusers, Movies
from django.contrib.auth.models import User

from django.http import HttpResponse


def login(request):
    if request.user.is_authenticated:
        player = request.user
        try:
            crap = Myusers.objects.get(email=player.email)
            if crap.choice is None:
                firsttime = 1
                return HttpResponse("No choices filled!")
            else :
                firsttime = 0
        except Myusers.DoesNotExist:
            user = Myusers()
            user.name = player.username
            user.email = player.email
            user.save()
            firsttime = 1

        crap = Myusers.objects.get(email=player.email)

        pk = crap.pointsfactor
        pk = pk+1
        pk = str(pk)

        if firsttime == 0:
            if crap.choice == "Movies":
               # question = get_object_or_404( Movies, pk = pk)
                questionmovies(request, pk)
               # return render(request, 'questions.html',{'question':question, 'pk':pk})

        return choose(request)
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

            case = 0
    #        return HttpResponse("correct ans!")
        else:
            case = 1
    #        return HttpResponse("No choices filled!")
    #    else:
    #        name = crap.name  

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
    if player.choice is None:
        player.choice = "Movies"
        player.save()
    #    return HttpResponse("lol saved as movies!")


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


