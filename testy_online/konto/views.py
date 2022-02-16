from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from aplikacja.models import Test, Answer
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from .forms import RegisterForm
from .models import Result


def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Utworzono konto, możesz się zalogować')
            return HttpResponseRedirect(reverse('konto:login'))
    else:
        form = RegisterForm()

    return render(req, 'konto/register.html', {'form': form})


def login(req):
    return render(req, 'konto/login.html')


@login_required
def profile(req):
    user = req.user.id
    try:
        results = Result.objects.filter(user=user).order_by('-completion_date')
    except ObjectDoesNotExist:
        results = None
    return render(req, 'konto/profile.html', context={'results': results})


@login_required
def send_test(req, test_id):
    test = Test.objects.get(pk=test_id)
    n = test.questions_number
    if len(req.POST)-1 != n:
        return render(req, 'aplikacja/error.html')

    score = 0
    for i in range(n):
        choice = req.POST[f'choice_{i+1}']
        answer = Answer.objects.get(pk=choice)
        if answer.is_correct:
            score += 1

    user = req.user
    result = Result(user=user, test=test, score=score, max_score=n)
    result.save()

    return HttpResponseRedirect(reverse('konto:result', args=(score, n)))


@login_required
def get_result(req, score, max_score):
    return render(req, 'konto/result.html', context={'score': score, 'max_score': max_score})
