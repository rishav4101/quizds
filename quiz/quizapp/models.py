from django.db import models


from django.contrib.auth.models import User

import datetime



# Create your models here.


class Myusers(models.Model):
    name = models.ForeignKey(to=User,on_delete=models.CASCADE)
    email = models.CharField(max_length=50,default=None)
    choice = models.CharField(max_length=30)
    pointsfactor = models.IntegerField(default=0)   # The no. of correct answers
    rank=models.IntegerField(null=True)
    lastcorrectans = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['-pointsfactor','lastcorrectans']

    def ranks(self):
        players=self.objects.all()
        rank=1
        for player in players:
            player.rank=rank
            rank +=1
        return players

    def scoreupdate(player):
        player.pointsfactor+=1
        player.save()

class Movies (models.Model):
    order = models.IntegerField(default=0, unique=True)
    question = models.CharField(max_length=500)
    islink = models.BooleanField(default=False)
    ispic = models.BooleanField(default=False)
    answer = models.CharField(max_length=50)
    day=models.IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.question)


    

class Series (models.Model):
    order = models.IntegerField(default=0, unique=True)
    question = models.CharField(max_length=500)
    islink = models.BooleanField(default=False)
    ispic = models.BooleanField(default=False)
    answer = models.CharField(max_length=50)
    day=models.IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.question)

class Books (models.Model):
    order = models.IntegerField(default=0, unique=True)
    question = models.CharField(max_length=500)
    islink = models.BooleanField(default=False)
    ispic = models.BooleanField(default=False)
    answer = models.CharField(max_length=50)
    day=models.IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.question)

    class Meta:
        ordering=['day','order']


    def check_ans(self,answer,question):
        answers=question.answer.split(",")
        for ans in answers:
            if answer==ans:
                return True
        return False

    def get_next_question(self,day,qno):
        question=self.objects.filter(day=day,question_no=qno)
        return question





