from django.shortcuts import render
from django.http import HttpResponse, request
import random

# Create your views here.


def index(request):
    return render(request, 'quiz/home.html')


def mathtopicselection(request):
    return render(request, 'quiz/mathtopicselection.html')


def numbersintro(request):
    return render(request, 'quiz/numbersintro.html')


def additionintro(request):
    return render(request, 'quiz/additionintro.html')


def numberquiz(request):
    return render(request, 'quiz/numbersquiz.html')


def additionquiz(request):
    return render(request, 'quiz/additionquiz.html')


def englishtopicselection(request):
    return render(request, 'quiz/englishtopicselection.html')


def a_e(request):
    return render(request, 'quiz/a_e.html')


def f_j(request):
    return render(request, 'quiz/f_j.html')


def k_o(request):
    return render(request, 'quiz/k_o.html')


def p_t(request):
    return render(request, 'quiz/p_t.html')


def u_z(request):
    return render(request, 'quiz/u_z.html')


def creativelearning(request):
    return render(request, 'quiz/creativelearning.html')
    
    
def creativelearningDev(request):
    return render(request, 'quiz/creativelearningDev.html')
    
    
def mathDraw(request):
    questions=[]
    operations=['+','-','/','*']
    
    for x in range(0, 5):
        first=random.randint(0, 9)
        second=random.randint(0, 9)
        
        questions.append(str(first)+operations[random.randint(0, 3)]+str(second))
    args = {}
    args['questions']=questions   
    return render(request, 'quiz/draw.html',args)