from django.shortcuts import render, redirect
from .models import Thought
from .forms import ThoughtForm

# Create your views here.


def get_thoughts(request):
    thoughts = Thought.objects.all()
    context = {
        'thoughts': thoughts
    }

    return render(request, 'thoughts/view_thoughts.html', context)


def add_thought(request):
    if request.method == 'POST':
        form = ThoughtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_thoughts')
    form = ThoughtForm()
    context = {
        'form': form
    }
    return render(request, 'thoughts/add_thought.html', context)
