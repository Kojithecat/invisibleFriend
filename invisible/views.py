from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Participant, Assignment
import random

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        Participant.objects.create(user=user)
        return redirect('login')
    return render(request, 'register.html')

def assign_secret_santa(request):
    participants = list(Participant.objects.all())
    random.shuffle(participants)

    for i in range(len(participants)):
        giver = participants[i]
        receiver = participants[(i + 1) % len(participants)]  # The next participant in the shuffled list
        Assignment.objects.create(giver=giver, receiver=receiver)
        giver.is_assigned = True
        giver.save()

    return redirect('view_assignment')

def view_assignment(request):
    participant = Participant.objects.get(user=request.user)
    assignment = Assignment.objects.get(giver=participant)
    context = {
        'receiver': assignment.receiver
    }
    return render(request, 'assignment.html', context)
