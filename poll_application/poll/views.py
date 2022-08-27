from django.shortcuts import render, redirect
from .models import Poll
from django.contrib.auth.models import User

from django.contrib import messages 



def index(request):
    poll = Poll.objects.all()
    context = {
        "poll" : poll,
    }
    return render(request, 'poll/index.html' , context)



def create(request):
    if request.method == "POST":
        question = request.POST.get('question')
        option_one = request.POST.get('optionone')
        option_two = request.POST.get('optiontwo')
        option_three = request.POST.get('optionthree')
        option_four = request.POST.get('optionfour')       

        poll = Poll(userid = request.user , question = question , option_one = option_one , option_two = option_two , option_three = option_three , option_four = option_four)
        poll.save()

        messages.success(request, "Poll created successfully") 
        
    return render(request, 'poll/create.html')



def vote(request, id):
    poll = Poll.objects.get(id = id)

    u = str(request)
    u = (u[-5:-2:1])

    if u == 'op1':
        print('option one')
        poll.option_one_count += 1

    elif u == 'op2':
        poll.option_one_count += 1

    elif u == 'op3':
        poll.option_one_count += 1

    elif u == 'op4':
        poll.option_one_count += 1

    poll.save()
    messages.success(request, "voted successfully") 
    return redirect('home')



def result(request):
    user = User.objects.get(username = request.user)
    poll = Poll.objects.filter(userid = request.user)
    context={
        "user" : user,
        "poll" : poll
    }

    return render(request, 'poll/profile.html' , context)
